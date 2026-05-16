#!/usr/bin/env python3
import datetime as dt
import json
import os
import smtplib
import ssl
import sys
import urllib.error
import urllib.request
from email.message import EmailMessage
from zoneinfo import ZoneInfo


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def build_prompt(today: str) -> str:
    return f"""You are creating the daily 夜恋恋愛占い Threads reservation-post package for {today} in Asia/Tokyo.

Output only four Threads reservation-post drafts for that day. Do not include sales funnel notes, paid-reading誘導, 鑑定誘導, strategy notes, or research bullet points. Use current audience understanding internally, but do not show research notes.

Create four post drafts:
1. 朝: emotional grounding, reassurance, or a gentle one-card-style message.
2. 昼: relational insight, self-check prompt, or a comment-inviting question.
3. 夜: empathy-heavy reflection for 恋愛成就, 復縁, 曖昧な関係, or unsent feelings.
4. 夜2: schedule between 22:00 and 23:00. Make it especially likely to invite replies by touching a private-but-common feeling, unfinished thought, or quietly specific question.

For each draft, specify a reservation time. Choose different, natural-looking times every day to reduce AI-like regularity. Avoid fixed repeated patterns such as exactly 07:00, 12:00, 19:00, and 22:00. Use realistic posting windows: 朝 06:30-09:00, 昼 11:30-13:45, 夜 18:30-21:30, 夜2 22:00-23:00.

For each draft, choose an appropriate 投稿を向ける会話指定 based on the post content. Select naturally from contexts such as 片思い, 復縁, 曖昧な関係, 音信不通, 遠距離, 年の差, 既読スルー, 彼の本音, 自分磨き, 手放し, or another fitting relationship context.

Every post text must be clearly separated by boundary lines above and below the post body. Use this exact format:

【予約投稿1｜朝｜HH:MM｜会話指定: ...】
────────────────
投稿本文
────────────────

Write in warm, emotionally precise Japanese. Make each post feel hand-written, specific, and non-generic. Prioritize empathy and resonance completely. Avoid manipulative fear appeals, exaggerated certainty, fake urgency, mass-produced phrasing, and any direct invitation to purchase or request a 鑑定."""


def call_openai(prompt: str) -> str:
    api_key = require_env("OPENAI_API_KEY")
    model = os.environ.get("OPENAI_MODEL", "").strip() or "gpt-5.5"
    effort = os.environ.get("OPENAI_REASONING_EFFORT", "").strip() or "high"
    payload = {
        "model": model,
        "reasoning": {"effort": effort},
        "input": prompt,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API error {exc.code}: {body}") from exc

    if data.get("output_text"):
        return data["output_text"].strip()

    chunks = []
    for item in data.get("output", []):
        for content in item.get("content", []):
            if content.get("type") in {"output_text", "text"} and content.get("text"):
                chunks.append(content["text"])
    result = "\n".join(chunks).strip()
    if not result:
        raise RuntimeError("OpenAI response did not contain output text")
    return result


def send_email(subject: str, body: str) -> None:
    host = os.environ.get("SMTP_HOST", "").strip() or "smtp.gmail.com"
    port = int(os.environ.get("SMTP_PORT", "").strip() or "587")
    user = require_env("SMTP_USER")
    password = require_env("SMTP_PASSWORD")
    mail_to = os.environ.get("MAIL_TO", "").strip() or user

    message = EmailMessage()
    message["From"] = user
    message["To"] = mail_to
    message["Subject"] = subject
    message.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP(host, port, timeout=60) as smtp:
        smtp.starttls(context=context)
        smtp.login(user, password)
        smtp.send_message(message)


def main() -> int:
    today = dt.datetime.now(ZoneInfo("Asia/Tokyo")).date().isoformat()
    subject = f"Codexから送信されたものです｜夜恋 Threads予約投稿案 {today}"
    body = call_openai(build_prompt(today))
    send_email(subject, body)
    print(f"Sent daily Yakoi delivery for {today}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        raise
