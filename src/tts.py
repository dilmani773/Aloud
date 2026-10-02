import io
from functools import lru_cache

from gtts import gTTS


def tts_gtts(text: str):
    buf = io.BytesIO()
    gTTS(text, lang="si").write_to_fp(buf)
    return buf.getvalue(), "audio/mp3"


@lru_cache(maxsize=1)
def _load_mms():
    from transformers import AutoTokenizer, VitsModel
    return (VitsModel.from_pretrained("facebook/mms-tts-sin"),
            AutoTokenizer.from_pretrained("facebook/mms-tts-sin"))


def tts_mms(text: str):
    import numpy as np
    import scipy.io.wavfile
    import torch
    model, tok = _load_mms()
    chunks = [s.strip() for s in text.replace("\n", ".").split(".") if s.strip()]
    waves = []
    for c in chunks:
        with torch.no_grad():
            waves.append(model(**tok(c, return_tensors="pt")).waveform[0].numpy())
        waves.append(np.zeros(int(model.config.sampling_rate * 0.3)))
    buf = io.BytesIO()
    scipy.io.wavfile.write(buf, model.config.sampling_rate, np.concatenate(waves).astype("float32"))
    return buf.getvalue(), "audio/wav"


def speak(text: str, engine: str = "gtts"):
    return tts_mms(text) if engine == "mms" else tts_gtts(text)
