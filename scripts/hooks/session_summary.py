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
log_path = os.path.join(log_dir, "hook-session-summary.txt")

os.makedirs(log_dir, exist_ok=True)

stamp = data.get("timestamp") or datetime.utcnow().isoformat() + "Z"
session_id = data.get("sessionId", "unknown")
transcript_path = data.get("transcript_path", "unknown")

line = f"{stamp} session={session_id} transcript={transcript_path}\n"

try:
    with open(log_path, "a", encoding="utf-8") as handle:
        handle.write(line)
except OSError:
    pass

sys.stdout.write(json.dumps({"continue": True}))
