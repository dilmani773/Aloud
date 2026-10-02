import base64
import json

import anthropic

from src.prompts import PROMPT

MODEL = "claude-sonnet-5-5"


def read_image(img_bytes: bytes, mime: str, api_key: str) -> dict:
    """Send a photo to Claude and get back Sinhala text as a dict."""
    client = anthropic.Anthropic(api_key=api_key)
    msg = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {"type": "base64", "media_type": mime,
                                          "data": base64.b64encode(img_bytes).decode()}},
            {"type": "text", "text": PROMPT},
        ]}],
    )
    raw = "".join(b.text for b in msg.content if b.type == "text")
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)
