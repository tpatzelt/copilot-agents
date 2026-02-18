#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime


def read_input():
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


data = read_input()

cwd = data.get("cwd") or os.getcwd()
log_dir = os.path.join(cwd, "artifacts")
log_path = os.path.join(log_dir, "hook-audit.log")

os.makedirs(log_dir, exist_ok=True)

stamp = data.get("timestamp") or datetime.utcnow().isoformat() + "Z"
tool_name = data.get("tool_name", "unknown")
tool_id = data.get("tool_use_id", "unknown")

line = f"{stamp} tool={tool_name} id={tool_id}\n"

try:
    with open(log_path, "a", encoding="utf-8") as handle:
        handle.write(line)
except OSError:
    pass

sys.stdout.write(json.dumps({"continue": True}))
