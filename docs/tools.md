# Tools and Approvals

VS Code agents can use built-in tools, MCP tools, and extension tools. You can
control which tools are available per request or per agent, and you can require
approval before tools execute.

## Tool types

- Built-in: search, codebase, problems, changes, terminal, fetch
- MCP: tools provided by local or remote MCP servers
- Extension tools: tools contributed by installed extensions

## Tool sets

Tool sets group related tools so you can enable them together. Example JSON:

```json
{
  "reader": {
    "tools": ["changes", "codebase", "problems", "usages"],
    "description": "Read-only context tools",
    "icon": "book"
  }
}
```

## Approval tips

- Keep auto-approval off for destructive tools.
- Review tool parameters before running terminal commands.
- Use hooks to enforce or override approvals.
