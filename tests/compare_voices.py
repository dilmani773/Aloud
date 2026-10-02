"""Week-1 voice test: read every photo in samples/ with both voices.
Usage: ANTHROPIC_API_KEY=... python -m tests.compare_voices
Output goes to tests/output/<file>_gtts.mp3 and <file>_mms.wav"""
import mimetypes
import os
from pathlib import Path

from src.reader import read_image
from src.tts import tts_gtts, tts_mms

out = Path("tests/output")
out.mkdir(parents=True, exist_ok=True)
key = os.environ["ANTHROPIC_API_KEY"]

for img in Path("samples").rglob("*"):
    if img.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
        continue
    r = read_image(img.read_bytes(), mimetypes.guess_type(img)[0], key)
    text = " ".join(p for p in [r.get("summary", ""), r.get("text", "")] if p)
    (out / f"{img.stem}.txt").write_text(text, encoding="utf-8")
    (out / f"{img.stem}_gtts.mp3").write_bytes(tts_gtts(text)[0])
    (out / f"{img.stem}_mms.wav").write_bytes(tts_mms(text)[0])
    print("done:", img.name)
