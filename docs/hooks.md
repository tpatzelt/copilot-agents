# Agent Hooks

Hooks let you run commands at agent lifecycle events to enforce policy, inject
context, or automate tasks. This repo includes sample hooks that are safe to run
and easy to customize.

## Configuration

- Hook config file: .github/hooks/agent-hooks.json
- Hook scripts: scripts/hooks
- Output artifacts: artifacts (ignored by git)

## Events used in this repo

- SessionStart: inject context and log session start
- PreToolUse: block dangerous commands before they run
- PostToolUse: append a tool audit entry
- Stop: write a basic session summary record

## Requirements

Hooks are in preview and require VS Code Insiders. See the official docs for
setup details and security guidance.
