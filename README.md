# Aloud 🔊

Take a photo of a letter, medicine box or bill. Aloud reads it out in Sinhala.

Built for elderly people in Sri Lanka who can no longer read small print.

## How it works

Photo → AI reads the text → English is translated to simple Sinhala → read aloud in Sinhala

- Long letters get a short summary first ("මේ ලියුමේ කියන්නේ...")
- Medicine labels add a spoken reminder to check the dose with a pharmacist
- Blurry photos get a spoken "please take the photo again"

## Run locally

```bash
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # add your API key
streamlit run app.py
```

## Compare Sinhala voices (gTTS vs Meta MMS)

```bash
pip install -r requirements-dev.txt
# put test photos in samples/letters, samples/medicine, samples/bills
ANTHROPIC_API_KEY=... python -m tests.compare_voices
```

## Project structure

```
app.py               Streamlit app
src/prompts.py       AI prompt and fixed Sinhala messages
src/reader.py        Photo to Sinhala text (Claude API)
src/tts.py           Sinhala voice (gTTS, MMS)
src/ui.py            Large, high-contrast styling
tests/               Voice comparison script
samples/             Test photos (not committed)
```

## Roadmap

- [x] Photo to Sinhala speech
- [x] Medicine safety reminder, retake prompt
- [ ] Test with elderly users
- [ ] "Read again" and "Read slowly" buttons
- [ ] Tamil support
- [ ] WhatsApp version: send a photo, get a voice note back

## Note

AI can misread text. Always confirm medicine doses with a pharmacist or doctor.
