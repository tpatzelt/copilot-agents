# Copilot Agents Showcase

Showcase repository for GitHub Copilot agent capabilities in VS Code. This repo
includes custom agents, hooks, and guided workflows that demonstrate planning,
implementation, review, and research patterns.

## What this repo demonstrates

- Custom agents with handoffs for multi-step flows
- Agent hooks for policy enforcement and automation
- Tool usage patterns, approvals, and tool sets
- Local, background, and cloud agent workflows
- Research and planning artifacts you can reuse

## Quickstart

1. Open the workspace in VS Code.
2. Ensure GitHub Copilot is enabled and agents are allowed in your settings.
3. Open the Chat view and choose Agent mode.
4. Pick a custom agent from the agent dropdown.
5. Try a workflow from docs/workflows.md.

## Repo map

- .github/agents: Custom agent definitions
- .github/hooks: Hook configuration
- scripts/hooks: Hook scripts used by the configuration
- docs: Guides and workflow examples
- artifacts: Hook output examples (ignored by git)

## Recommended demo flows

- Plan -> Implement -> Review -> Release Notes (use handoffs)
- Research -> Plan -> Implement
- Diagnose failing tests with Problem, Search, and Edit tools

## References

- https://code.visualstudio.com/docs/copilot/agents/overview
- https://code.visualstudio.com/docs/copilot/agents/agent-tools
- https://code.visualstudio.com/docs/copilot/customization/custom-agents
- https://code.visualstudio.com/docs/copilot/customization/hooks
