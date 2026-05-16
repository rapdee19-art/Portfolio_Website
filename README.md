# 夜恋 Codex Workspace

This repository is a lightweight handoff workspace for 夜恋 Threads operations.

The goal is to keep the local Mac as light as possible:

- Keep source notes and operational prompts in GitHub.
- Run recurring delivery as a scheduled Codex automation, not as a foreground session.
- Use Codex Web or remote/worktree execution for heavier edits, research, or future tooling after GitHub is connected.
- Avoid local dev servers, browser automation, and dependency installs unless a task explicitly needs them.

See [CLOUD_AUTOMATION_PLAN.md](CLOUD_AUTOMATION_PLAN.md) for the path to run the morning delivery from cloud/worktree execution when the Mac is asleep or Codex desktop is closed.

## Current Daily Automation

Automation name: `夜恋 Threads投稿案 毎朝6時納品`

Expected behavior:

- Runs once each morning at 06:00 Asia/Tokyo.
- Runs through cloud/worktree execution after GitHub connection is verified.
- Produces three Threads drafts: morning, noon, and night.
- Sends exactly one Gmail delivery for each scheduled run.
- Includes `Codexから送信されたものです` in the Gmail subject.
- Does not wait, poll, monitor, or keep a long-running local process alive.

## Recommended Workflow

1. Keep this repo small and sync it to GitHub.
2. Use Codex Web for heavier work when the Intel Mac feels slow.
3. Use the local Codex app for quick checks, automation edits, and final review.
4. Commit only useful prompts, notes, templates, and lightweight configuration.
5. Keep the daily Gmail automation on worktree execution after the GitHub remote is connected and verified.

## What Belongs Here

- Prompt templates
- Content direction notes
- Audience research summaries
- Delivery process notes
- Lightweight scripts only if they are genuinely needed

## What Should Stay Out

- Large generated files
- Browser caches
- Local build outputs
- Dependency folders
- Long-running logs
- Secrets or API keys
