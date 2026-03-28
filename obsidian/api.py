"""
Obsidian Local REST API Client for Daily Agent academic workflow.
Allows Claude to read, create, and search notes in the Obsidian vault.

Requires: Obsidian running with "Local REST API" community plugin enabled.

Usage (from CLI):
    python obsidian/api.py read "Projects/my-note.md"
    python obsidian/api.py create "Research/new-note.md" "# Title\nContent"
    python obsidian/api.py append "Research/note.md" "\n## New Section\nMore content"
    python obsidian/api.py delete "Research/old-note.md"
    python obsidian/api.py search "machine learning"
    python obsidian/api.py list
    python obsidian/api.py list "Research/"
    python obsidian/api.py daily
    python obsidian/api.py daily_append "- New task from Claude"
    python obsidian/api.py status
"""

import json
import os
import sys
import urllib3
from pathlib import Path

import requests

# Suppress InsecureRequestWarning for self-signed cert
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_HOST = "https://127.0.0.1"
DEFAULT_PORT = "27124"


def load_config():
    """Load Obsidian REST API credentials from .env file."""
    env_path = Path(__file__).resolve().parent.parent / ".env"
    config = {}
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()

    api_key = config.get("OBSIDIAN_API_KEY") or os.environ.get("OBSIDIAN_API_KEY")
    host = config.get("OBSIDIAN_HOST") or os.environ.get("OBSIDIAN_HOST") or DEFAULT_HOST
    port = config.get("OBSIDIAN_PORT") or os.environ.get("OBSIDIAN_PORT") or DEFAULT_PORT

    if not api_key:
        print("ERROR: OBSIDIAN_API_KEY must be set in .env or environment.")
        print("Install 'Local REST API' plugin in Obsidian, then copy the API key from plugin settings.")
        sys.exit(1)

    return api_key, f"{host}:{port}"


def _headers(api_key, content_type="application/json"):
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": content_type,
    }


def _request(method, endpoint, api_key, base_url, data=None, content_type="application/json"):
    """Make a request to the Obsidian Local REST API."""
    url = f"{base_url}{endpoint}"
    headers = _headers(api_key, content_type)
    resp = requests.request(method, url, headers=headers, data=data, verify=False)
    resp.raise_for_status()
    return resp


# --- Core Functions ---

def check_status():
    """Check if Obsidian REST API is reachable."""
    api_key, base_url = load_config()
    try:
        resp = requests.get(f"{base_url}/", headers=_headers(api_key), verify=False, timeout=3)
        return {"status": "connected", "code": resp.status_code}
    except requests.ConnectionError:
        return {"status": "disconnected", "error": "Obsidian is not running or Local REST API plugin is not enabled."}


def read_note(path):
    """Read a note's markdown content by vault-relative path."""
    api_key, base_url = load_config()
    resp = _request("GET", f"/vault/{path}", api_key, base_url)
    return resp.text


def create_note(path, content):
    """Create or overwrite a note at the given path."""
    api_key, base_url = load_config()
    _request("PUT", f"/vault/{path}", api_key, base_url, data=content.encode("utf-8"), content_type="text/markdown")
    return {"status": "created", "path": path}


def append_to_note(path, content):
    """Append content to an existing note."""
    api_key, base_url = load_config()
    _request("PATCH", f"/vault/{path}", api_key, base_url, data=content.encode("utf-8"), content_type="text/markdown")
    return {"status": "appended", "path": path}


def delete_note(path):
    """Delete a note by path."""
    api_key, base_url = load_config()
    _request("DELETE", f"/vault/{path}", api_key, base_url)
    return {"status": "deleted", "path": path}


def search_notes(query):
    """Search notes by filename/content."""
    api_key, base_url = load_config()
    resp = _request("POST", "/search/simple/", api_key, base_url, data=json.dumps({"query": query}))
    return resp.json()


def list_notes(folder=None):
    """List all markdown files in the vault, optionally filtered by folder prefix."""
    api_key, base_url = load_config()
    resp = _request("GET", "/vault/", api_key, base_url)
    files = resp.json().get("files", [])
    md_files = [f for f in files if f.endswith(".md")]
    if folder:
        folder = folder.rstrip("/") + "/"
        md_files = [f for f in md_files if f.startswith(folder)]
    return md_files


def get_daily_note():
    """Get today's daily note content."""
    api_key, base_url = load_config()
    resp = _request("GET", "/periodic/daily/", api_key, base_url)
    return resp.text


def append_to_daily(content):
    """Append content to today's daily note."""
    api_key, base_url = load_config()
    _request("PATCH", "/periodic/daily/", api_key, base_url, data=content.encode("utf-8"), content_type="text/markdown")
    return {"status": "appended", "target": "daily note"}


def get_active_note():
    """Get the currently open/active note in Obsidian."""
    api_key, base_url = load_config()
    resp = _request("GET", "/active/", api_key, base_url)
    return resp.text


# --- Literature Note Creation ---

def create_literature_note(folder, item_data, annotations=None):
    """
    Create a structured literature note from Zotero item data.

    Args:
        folder: Vault folder path (e.g., "Research/Literature")
        item_data: Dict from zotero api.get_item()
        annotations: List of dicts from zotero api.get_annotations()
    """
    title = item_data.get("title", "Untitled")
    safe_title = "".join(c if c.isalnum() or c in " -_" else "" for c in title)[:80]
    filename = f"{folder.rstrip('/')}/{safe_title}.md"

    # Build frontmatter
    lines = [
        "---",
        f'title: "{title}"',
        f'authors: "{item_data.get("authors", "")}"',
        f'year: "{item_data.get("year", "")}"',
        f'doi: "{item_data.get("doi", "")}"',
        f'zotero_key: "{item_data.get("key", "")}"',
        f'type: "{item_data.get("type", "")}"',
        f'publication: "{item_data.get("publication", "")}"',
        f'tags: [{", ".join(item_data.get("tags", []))}]',
        f'date_created: "{__import__("datetime").date.today().isoformat()}"',
        "status: unread",
        "---",
        "",
        f"# {title}",
        "",
        f"**Authors:** {item_data.get('authors', '')}",
        f"**Year:** {item_data.get('year', '')}",
        f"**Publication:** {item_data.get('publication', '')}",
        f"**DOI:** {item_data.get('doi', '')}",
        f"**Zotero:** [Open in Zotero](zotero://select/items/{item_data.get('key', '')})",
        "",
    ]

    # Abstract
    abstract = item_data.get("abstract", "")
    if abstract:
        lines += ["## Abstract", "", abstract, ""]

    # Annotations from Zotero
    if annotations:
        highlights = [a for a in annotations if a.get("type") == "highlight"]
        notes = [a for a in annotations if a.get("type") in ("note", "")]

        if highlights:
            lines += ["## Highlights", ""]
            for h in highlights:
                text = h.get("text", "")
                comment = h.get("comment", "")
                page = h.get("page", "")
                page_ref = f" (p.{page})" if page else ""
                lines.append(f"> {text}{page_ref}")
                if comment:
                    lines.append(f"> **Note:** {comment}")
                lines.append("")

        if notes:
            lines += ["## Notes from Zotero", ""]
            for n in notes:
                lines.append(f"- {n.get('text', '')}")
            lines.append("")

    # Sections for the researcher to fill
    lines += [
        "## Key Arguments",
        "",
        "- ",
        "",
        "## Methodology",
        "",
        "- ",
        "",
        "## Findings",
        "",
        "- ",
        "",
        "## My Thoughts",
        "",
        "- ",
        "",
        "## Connections",
        "",
        "- Related: ",
        "",
    ]

    content = "\n".join(lines)
    return create_note(filename, content)


# --- CLI ---

def _print(data):
    if isinstance(data, str):
        print(data)
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "status":
        _print(check_status())
    elif cmd == "read" and len(sys.argv) >= 3:
        _print(read_note(sys.argv[2]))
    elif cmd == "create" and len(sys.argv) >= 4:
        _print(create_note(sys.argv[2], sys.argv[3]))
    elif cmd == "append" and len(sys.argv) >= 4:
        _print(append_to_note(sys.argv[2], sys.argv[3]))
    elif cmd == "delete" and len(sys.argv) >= 3:
        _print(delete_note(sys.argv[2]))
    elif cmd == "search" and len(sys.argv) >= 3:
        _print(search_notes(" ".join(sys.argv[2:])))
    elif cmd == "list":
        folder = sys.argv[2] if len(sys.argv) >= 3 else None
        _print(list_notes(folder))
    elif cmd == "daily":
        _print(get_daily_note())
    elif cmd == "daily_append" and len(sys.argv) >= 3:
        _print(append_to_daily(sys.argv[2]))
    else:
        print(__doc__)
        sys.exit(1)
