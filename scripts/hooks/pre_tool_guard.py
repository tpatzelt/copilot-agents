#!/usr/bin/env python3
import json
import re
import sys


def read_input():
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def emit(payload):
    sys.stdout.write(json.dumps(payload))


data = read_input()

tool_name = str(data.get("tool_name", "")).lower()
tool_input = data.get("tool_input", {})
input_text = json.dumps(tool_input, ensure_ascii=True)

danger_patterns = [
    r"rm\s+-rf\s+/",
    r"\bdrop\s+table\b",
    r"\btruncate\s+table\b",
]

is_dangerous = any(re.search(p, input_text, flags=re.IGNORECASE) for p in danger_patterns)

if is_dangerous:
    emit(
        {
            "continue": True,
            "stopReason": "Security policy violation",
            "systemMessage": "Blocked a destructive operation. Review the request and try a safer alternative.",
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": "Matched destructive pattern in tool input.",
                "additionalContext": f"tool_name={tool_name}"
            },
        }
    )
else:
    emit({"continue": True})
