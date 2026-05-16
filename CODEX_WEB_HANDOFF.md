# Codex Web Handoff

Use this repo as the shared source of truth when moving work away from the local Mac.

## Lightweight Local Setup

The local machine should only need:

- Git
- The Codex desktop app
- Access to the scheduled automation

Avoid installing project dependencies unless a future task truly needs them.

The daily Gmail automation should use worktree execution after this repository has a GitHub remote. The scheduled run should wake in the cloud/worktree environment once per day and should not depend on the Mac being awake.

## GitHub Setup

Once a GitHub repository exists, add it as the remote:

```bash
git remote add origin git@github.com:OWNER/REPO.git
git branch -M main
git push -u origin main
```

If SSH is not set up, use the HTTPS remote shown by GitHub instead.

## Codex Web Use

For heavier work:

1. Open the GitHub repository in Codex Web.
2. Ask Codex Web to make the change in a branch.
3. Review the diff or pull request.
4. Pull the final lightweight changes locally only when needed.

After GitHub is connected and a remote worktree run has been verified, keep the daily automation on worktree execution.

The cloud migration checklist lives in [CLOUD_AUTOMATION_PLAN.md](CLOUD_AUTOMATION_PLAN.md).

## Daily Automation Policy

The morning delivery should remain a scheduled one-shot run:

- No live waiting until 06:00.
- No continuous monitoring.
- No local server.
- No browser session unless a specific task requires visual verification.
- One Gmail delivery per scheduled run.
