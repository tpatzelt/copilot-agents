# Custom Agents Catalog

These agents live in .github/agents and show different task profiles.

## Planner

- Goal: produce an implementation plan with risks and tests
- Hand off to: Implementation, Reviewer
- Best for: scoping work before changes are made

## Implementation

- Goal: implement changes and update tests
- Hand off to: Reviewer, Release Notes
- Best for: multi-file edits and test runs

## Reviewer

- Goal: review changes for risks, regressions, and test gaps
- Hand off to: Implementation for fixes
- Best for: pre-PR quality checks

## Researcher

- Goal: gather external context with sources and summary
- Hand off to: Planner
- Best for: dependency research or API exploration

## Release Notes

- Goal: summarize changes from the working tree or PR
- Hand off to: Reviewer for final wording
- Best for: change summaries and announcements
