#!/usr/bin/env python3
"""Trello API helper for Claude Code skill.

Usage from Bash tool:
    python3 .claude/skills/trello/scripts/trello_api.py <command> [args...]

Commands:
    update_card <card_id> --name "title" --desc "description"
    get_card <card_id>
    move_card <card_id> <list_id>
    add_comment <card_id> "comment text"
    search <query>
    list_cards <list_id>
    create_card <list_id> --name "title" [--desc "desc"] [--labels "id1,id2"]
    add_label <card_id> <label_id>
    remove_label <card_id> <label_id>
    mark_done <card_id>
    mark_undone <card_id>

Requires TRELLO_API_KEY and TRELLO_TOKEN environment variables.
"""

import json
import os
import sys
import urllib.parse
import urllib.request


API_BASE = "https://api.trello.com/1"
BOARD_ID = "698cc371e8291dcffe3895a8"  # Q1 Prototyping
GITHUB_BASE = "https://github.com/Record360/record-paas/blob/main"


def get_auth():
    key = os.environ.get("TRELLO_API_KEY")
    token = os.environ.get("TRELLO_TOKEN")
    if not key or not token:
        print("Error: TRELLO_API_KEY and TRELLO_TOKEN must be set", file=sys.stderr)
        sys.exit(1)
    return key, token


def api_request(method, path, params=None, data=None):
    key, token = get_auth()
    query = {"key": key, "token": token}
    if params:
        query.update(params)
    url = f"{API_BASE}{path}?{urllib.parse.urlencode(query)}"

    body = json.dumps(data).encode() if data else None
    headers = {"Content-Type": "application/json"} if data else {}
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    resp = urllib.request.urlopen(req)
    raw = resp.read()
    if not raw:
        return None
    return json.loads(raw)


def get_card(card_id):
    result = api_request("GET", f"/cards/{card_id}", params={"fields": "name,desc,shortUrl,idList"})
    print(json.dumps(result, indent=2))


def update_card(card_id, **fields):
    result = api_request("PUT", f"/cards/{card_id}", data=fields)
    print(f"Updated: {result['name']}")
    print(f"URL: {result['shortUrl']}")


def move_card(card_id, list_id):
    result = api_request("PUT", f"/cards/{card_id}", data={"idList": list_id})
    print(f"Moved: {result['name']}")


def add_comment(card_id, text):
    result = api_request("POST", f"/cards/{card_id}/actions/comments", data={"text": text})
    print(f"Comment added: {result['id']}")


def search(query):
    result = api_request("GET", "/search", params={
        "query": query,
        "modelTypes": "cards",
        "card_fields": "name,desc,shortUrl,idList",
        "idBoards": BOARD_ID,
    })
    for card in result.get("cards", []):
        print(f"  {card['name']}")
        print(f"  {card['shortUrl']}")
        print()


def list_cards(list_id):
    result = api_request("GET", f"/lists/{list_id}/cards", params={
        "fields": "name,desc,shortUrl,labels",
    })
    for card in result:
        print(f"  {card['name']}")
        print(f"  {card['shortUrl']}")
        print()


def create_card(list_id, name, desc="", labels=None):
    data = {"idList": list_id, "name": name, "desc": desc}
    if labels:
        data["idLabels"] = labels
    result = api_request("POST", "/cards", data=data)
    print(json.dumps({"id": result["id"], "shortUrl": result["shortUrl"]}))


def add_label(card_id, label_id):
    api_request("POST", f"/cards/{card_id}/idLabels", data={"value": label_id})
    print(f"Label {label_id} added to card {card_id}")


def remove_label(card_id, label_id):
    api_request("DELETE", f"/cards/{card_id}/idLabels/{label_id}")
    print(f"Label {label_id} removed from card {card_id}")


def mark_done(card_id):
    result = api_request("PUT", f"/cards/{card_id}", data={"dueComplete": True})
    print(f"Done: {result['name']}")


def mark_undone(card_id):
    result = api_request("PUT", f"/cards/{card_id}", data={"dueComplete": False})
    print(f"Undone: {result['name']}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "get_card":
        get_card(sys.argv[2])
    elif cmd == "update_card":
        card_id = sys.argv[2]
        fields = {}
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--name":
                fields["name"] = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--desc":
                fields["desc"] = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        update_card(card_id, **fields)
    elif cmd == "move_card":
        move_card(sys.argv[2], sys.argv[3])
    elif cmd == "add_comment":
        add_comment(sys.argv[2], sys.argv[3])
    elif cmd == "search":
        search(sys.argv[2])
    elif cmd == "list_cards":
        list_cards(sys.argv[2])
    elif cmd == "create_card":
        list_id = sys.argv[2]
        name = None
        desc = ""
        labels = None
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--name":
                name = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--desc":
                desc = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--labels":
                labels = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        if not name:
            print("Error: --name is required", file=sys.stderr)
            sys.exit(1)
        create_card(list_id, name, desc=desc, labels=labels)
    elif cmd == "add_label":
        add_label(sys.argv[2], sys.argv[3])
    elif cmd == "remove_label":
        remove_label(sys.argv[2], sys.argv[3])
    elif cmd == "mark_done":
        mark_done(sys.argv[2])
    elif cmd == "mark_undone":
        mark_undone(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
