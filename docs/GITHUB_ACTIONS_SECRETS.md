# GitHub Actions Secrets

This repository includes a true cloud scheduled workflow:

`.github/workflows/yakoi-daily.yml`

It runs at 21:00 UTC, which is 06:00 Asia/Tokyo.

## Required Secrets

Add these in GitHub:

`Settings` -> `Secrets and variables` -> `Actions` -> `New repository secret`

- `OPENAI_API_KEY`: OpenAI API key for generating the daily drafts.
- `SMTP_USER`: Gmail address used to send the message.
- `SMTP_PASSWORD`: Gmail app password or SMTP password.
- `MAIL_TO`: recipient email address.

Optional:

- `SMTP_HOST`: defaults to `smtp.gmail.com`.
- `SMTP_PORT`: defaults to `587`.

## Optional Variables

Add this under repository variables if the default model needs to change:

- `OPENAI_MODEL`: defaults to `gpt-5.5` in the script.

## Notes

ChatGPT Plus does not automatically provide an OpenAI API key. API usage may be billed separately from ChatGPT Plus.

For Gmail, a normal account password may not work. A Gmail app password is usually required.
