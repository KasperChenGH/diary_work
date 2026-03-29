"""
Zotero API Client for Daily Agent academic workflow.
Allows Claude to search, read, and pull annotations from Zotero.

Usage (from CLI):
    python zotero/api.py search "machine learning"
    python zotero/api.py recent 10
    python zotero/api.py item ITEM_KEY
    python zotero/api.py annotations ITEM_KEY
    python zotero/api.py collections
    python zotero/api.py collection COLLECTION_KEY
    python zotero/api.py tags
    python zotero/api.py items_by_tag "tag_name"
"""

import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

BASE_URL = "https://api.zotero.org"


def load_config():
    """Load Zotero API credentials from environment."""
    api_key = os.environ.get("ZOTERO_API_KEY")
    user_id = os.environ.get("ZOTERO_USER_ID")

    if not api_key or not user_id:
        print("ERROR: ZOTERO_API_KEY and ZOTERO_USER_ID must be set in .env or environment.")
        print("Get your API key at: https://www.zotero.org/settings/keys/new")
        print("Find your user ID at: https://www.zotero.org/settings/keys")
        sys.exit(1)

    return api_key, user_id


def _headers(api_key):
    return {
        "Zotero-API-Version": "3",
        "Zotero-API-Key": api_key,
    }


def _get(api_key, user_id, endpoint, params=None):
    """Make a GET request to the Zotero API."""
    url = f"{BASE_URL}/users/{user_id}{endpoint}"
    resp = requests.get(url, headers=_headers(api_key), params=params or {}, timeout=30)
    resp.raise_for_status()
    return resp.json()


# --- Core Functions ---

def search_items(query, limit=10):
    """Search Zotero library by query string. Returns top-level items."""
    api_key, user_id = load_config()
    items = _get(api_key, user_id, "/items/top", {"q": query, "limit": limit, "format": "json"})
    return [_format_item(item) for item in items]


def get_recent_items(limit=10):
    """Get most recently added items."""
    api_key, user_id = load_config()
    items = _get(api_key, user_id, "/items/top", {
        "limit": limit,
        "sort": "dateAdded",
        "direction": "desc",
        "format": "json",
    })
    return [_format_item(item) for item in items]


def get_item(item_key):
    """Get full details of a single item by key."""
    api_key, user_id = load_config()
    item = _get(api_key, user_id, f"/items/{item_key}")
    return _format_item_full(item)


def get_annotations(item_key):
    """Get all annotations (highlights, notes) for an item.

    Checks two levels:
    1. Direct children of the item (top-level notes)
    2. Children of any PDF attachments (actual PDF highlights & inline notes)

    Returns a list sorted by page number, with attachment_key included so
    callers can build zotero://open-pdf deep links.
    """
    api_key, user_id = load_config()
    children = _get(api_key, user_id, f"/items/{item_key}/children", {"format": "json"})
    annotations = []

    for child in children:
        data = child.get("data", {})
        item_type = data.get("itemType", "")

        if item_type == "annotation":
            # Direct annotation child (rare but possible)
            annotations.append({
                "type": data.get("annotationType", ""),
                "text": data.get("annotationText", ""),
                "comment": data.get("annotationComment", ""),
                "color": data.get("annotationColor", ""),
                "page": data.get("annotationPageLabel", ""),
                "attachment_key": child.get("key", ""),
            })

        elif item_type == "note":
            # Top-level note attached to the item
            annotations.append({
                "type": "note",
                "text": data.get("note", ""),
                "comment": "",
                "color": "",
                "page": "",
                "attachment_key": "",
            })

        elif item_type == "attachment":
            # Dig into PDF attachment for highlights / inline notes
            att_key = child["key"]
            try:
                pdf_children = _get(api_key, user_id, f"/items/{att_key}/children", {"format": "json"})
            except Exception:
                continue
            for ann in pdf_children:
                ann_data = ann.get("data", {})
                if ann_data.get("itemType") == "annotation":
                    annotations.append({
                        "type": ann_data.get("annotationType", ""),
                        "text": ann_data.get("annotationText", ""),
                        "comment": ann_data.get("annotationComment", ""),
                        "color": ann_data.get("annotationColor", ""),
                        "page": ann_data.get("annotationPageLabel", ""),
                        "attachment_key": att_key,
                        "annotation_key": ann["key"],
                    })

    # Sort by page number (non-numeric pages sort to end)
    def _page_sort(a):
        try:
            return int(a.get("page") or 9999)
        except ValueError:
            return 9999

    annotations.sort(key=_page_sort)
    return annotations


def get_collections():
    """List all collections in the library."""
    api_key, user_id = load_config()
    collections = _get(api_key, user_id, "/collections", {"format": "json"})
    return [
        {
            "key": c["data"]["key"],
            "name": c["data"]["name"],
            "parent": c["data"].get("parentCollection", ""),
            "item_count": c["meta"].get("numItems", 0),
        }
        for c in collections
    ]


def get_items_in_collection(collection_key, limit=100):
    """Get items in a specific collection."""
    api_key, user_id = load_config()
    items = _get(api_key, user_id, f"/collections/{collection_key}/items/top", {
        "limit": limit,
        "format": "json",
    })
    return [_format_item(item) for item in items]


def get_tags():
    """List all tags in the library."""
    api_key, user_id = load_config()
    tags = _get(api_key, user_id, "/tags", {"format": "json"})
    return [{"tag": t["tag"], "count": t["meta"].get("numItems", 0)} for t in tags]


def get_items_by_tag(tag, limit=25):
    """Get items with a specific tag."""
    api_key, user_id = load_config()
    items = _get(api_key, user_id, "/items/top", {
        "tag": tag,
        "limit": limit,
        "format": "json",
    })
    return [_format_item(item) for item in items]


# --- Formatting Helpers ---

def _parse_authors(creators):
    return ", ".join(
        f"{c.get('lastName', '')}, {c.get('firstName', '')}" if c.get("lastName") else c.get("name", "")
        for c in creators
    )


def _format_item(item):
    """Format a Zotero item into a clean summary dict."""
    data = item.get("data", {})
    authors = _parse_authors(data.get("creators", []))
    return {
        "key": data.get("key", ""),
        "title": data.get("title", ""),
        "authors": authors,
        "year": data.get("date", ""),
        "type": data.get("itemType", ""),
        "tags": [t["tag"] for t in data.get("tags", [])],
        "abstract": data.get("abstractNote", "")[:200] + "..." if len(data.get("abstractNote", "")) > 200 else data.get("abstractNote", ""),
        "doi": data.get("DOI", ""),
        "url": data.get("url", ""),
    }


def _format_item_full(item):
    """Format a Zotero item with all details."""
    data = item.get("data", {})
    authors = _parse_authors(data.get("creators", []))
    return {
        "key": data.get("key", ""),
        "title": data.get("title", ""),
        "authors": authors,
        "year": data.get("date", ""),
        "type": data.get("itemType", ""),
        "tags": [t["tag"] for t in data.get("tags", [])],
        "abstract": data.get("abstractNote", ""),
        "doi": data.get("DOI", ""),
        "url": data.get("url", ""),
        "publication": data.get("publicationTitle", ""),
        "volume": data.get("volume", ""),
        "issue": data.get("issue", ""),
        "pages": data.get("pages", ""),
        "language": data.get("language", ""),
        "date_added": data.get("dateAdded", ""),
        "date_modified": data.get("dateModified", ""),
    }


# --- CLI ---

def _print_json(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "search" and len(sys.argv) >= 3:
        query = " ".join(sys.argv[2:])
        _print_json(search_items(query))
    elif cmd == "recent":
        limit = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
        _print_json(get_recent_items(limit))
    elif cmd == "item" and len(sys.argv) >= 3:
        _print_json(get_item(sys.argv[2]))
    elif cmd == "annotations" and len(sys.argv) >= 3:
        _print_json(get_annotations(sys.argv[2]))
    elif cmd == "collections":
        _print_json(get_collections())
    elif cmd == "collection" and len(sys.argv) >= 3:
        _print_json(get_items_in_collection(sys.argv[2]))
    elif cmd == "tags":
        _print_json(get_tags())
    elif cmd == "items_by_tag" and len(sys.argv) >= 3:
        _print_json(get_items_by_tag(sys.argv[2]))
    else:
        print(__doc__)
        sys.exit(1)
