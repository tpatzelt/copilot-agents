# Hook Scripts

These scripts are referenced by .github/hooks/agent-hooks.json.

- pre_tool_guard.py: blocks destructive commands based on tool input
- post_tool_log.py: appends a simple tool audit line
- session_context.py: injects a short system message at session start
- session_summary.py: writes a session summary line on stop

Scripts are intentionally small and safe to modify for your environment.
