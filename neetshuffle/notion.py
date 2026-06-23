"""Minimal Notion API client (standard library only).

Used to mirror your solved problems into a Notion database as nicely-formatted
rows. We deliberately avoid the official SDK so neetshuffle keeps zero runtime
dependencies; everything here is urllib + json.
"""

import json
import urllib.error
import urllib.request

API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
TIMEOUT = 20  # seconds; don't hang forever on a flaky network

# Notion's allowed select-option colors (minus "default"); topics get one each.
_COLORS = ["blue", "green", "orange", "purple", "pink",
           "red", "yellow", "brown", "gray"]


class NotionError(Exception):
    """Raised for any non-success Notion API response or transport error."""

    def __init__(self, message, status=None):
        super().__init__(message)
        self.status = status


def _request(method, path, token, payload=None):
    url = API_BASE + path
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Notion-Version", NOTION_VERSION)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            err = json.loads(exc.read().decode("utf-8"))
            detail = err.get("message") or err.get("code") or ""
        except Exception:
            pass
        msg = "Notion API {} {}".format(exc.code, exc.reason)
        if detail:
            msg += ": " + detail
        raise NotionError(msg, status=exc.code)
    except urllib.error.URLError as exc:
        raise NotionError("could not reach Notion ({})".format(exc.reason))


def topic_color(topics, topic):
    """Stable color for a topic based on its position in the topic list."""
    try:
        idx = topics.index(topic)
    except ValueError:
        idx = 0
    return _COLORS[idx % len(_COLORS)]


def verify_token(token):
    """Confirm the token works; returns the bot/integration name."""
    me = _request("GET", "/users/me", token)
    return (me.get("bot", {}).get("owner", {}) and me.get("name")) or "integration"


def get_database(token, database_id):
    return _request("GET", "/databases/" + database_id, token)


def create_database(token, parent_page_id, topics, title="NeetCode 150 Progress"):
    """Create a nicely-structured progress database under a parent page.

    Returns the new database id."""
    properties = {
        "Problem": {"title": {}},
        "Topic": {"select": {"options": [
            {"name": t, "color": topic_color(topics, t)} for t in topics
        ]}},
        "Link": {"url": {}},
        "Solved on": {"date": {}},
        "Status": {"select": {"options": [
            {"name": "Solved", "color": "green"},
        ]}},
    }
    payload = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "icon": {"type": "emoji", "emoji": "🧩"},
        "title": [{"type": "text", "text": {"content": title}}],
        "properties": properties,
    }
    db = _request("POST", "/databases", token, payload)
    return db["id"]


def add_problem(token, database_id, name, url, topic, solved_on=None):
    """Add one solved problem as a row. Returns the new page id."""
    props = {
        "Problem": {"title": [{"type": "text", "text": {"content": name}}]},
        "Link": {"url": url},
        "Topic": {"select": {"name": topic}},
        "Status": {"select": {"name": "Solved"}},
    }
    if solved_on:
        props["Solved on"] = {"date": {"start": solved_on}}
    payload = {
        "parent": {"type": "database_id", "database_id": database_id},
        "icon": {"type": "emoji", "emoji": "✅"},
        "properties": props,
    }
    page = _request("POST", "/pages", token, payload)
    return page["id"]
