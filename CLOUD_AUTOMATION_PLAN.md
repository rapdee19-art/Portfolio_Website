# Cloud Automation Plan

Goal: run the daily 夜恋 Threads Gmail delivery even when the MacBook is asleep or the Codex desktop app is closed.

## Target Architecture

- GitHub stores this lightweight workspace.
- Codex cron automation uses `worktree` execution.
- The scheduled job wakes in Codex cloud/worktree execution at 06:00 Asia/Tokyo.
- Gmail delivery is sent from the authenticated Gmail connector.
- The local Mac is only used for setup, review, and occasional edits.

## Current Status

This local repository now points at the GitHub repository:

`https://github.com/rapdee19-art/-.git`

The local terminal cannot push or fetch over HTTPS because it has no GitHub credential prompt available. Repository files were therefore created through the authenticated GitHub connector.

## Migration Steps

1. Keep the lightweight workspace files in GitHub.
2. Update automation `threads-6` from `local` execution to `worktree` execution.
3. Verify the next scheduled run or run a short test automation.
4. Keep Gmail as the delivery target unless Gmail delivery fails in cloud execution.

## Fallback Options

If Gmail delivery is unavailable from cloud/worktree execution:

- Deliver to the current Codex thread as a heartbeat-style follow-up if the product supports that destination for the desired schedule.
- Use GitHub Issues as the cloud inbox for daily drafts.
- Use a repository file or dated Markdown note as the delivery artifact.

ChatGPT Project delivery is not directly configurable from this workspace unless a connector or product automation target exposes it.
