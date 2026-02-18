#!/usr/bin/env python3
import json
import sys


def read_input():
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


data = read_input()

message = (
    "Hook active: session context injected from repository. "
    "See docs/hooks.md for configuration details."
)

payload = {
    "continue": True,
    "systemMessage": message,
}

sys.stdout.write(json.dumps(payload))
