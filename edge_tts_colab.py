# Google Colab: paste into a cell after running   !pip install -q edge-tts nest_asyncio
import asyncio
import os

import edge_tts
import nest_asyncio
from google.colab import files

nest_asyncio.apply()  # lets asyncio run inside Colab's already-running event loop

# ================= SETTINGS =================
VOICE  = "en-US-GuyNeural"  # see the voice table in the README
RATE   = "+0%"              # speaking speed, e.g. "-10%" slower, "+15%" faster
PITCH  = "+0Hz"             # e.g. "-2Hz" deeper, "+3Hz" higher
VOLUME = "+0%"
LIST_VOICES = None          # e.g. "ur-" or "hi-": print matching voices instead of making audio
# ============================================


async def list_voices(prefix):
    voices = await edge_tts.list_voices()
    found = [v for v in voices if v["ShortName"].startswith(prefix)]
    for v in found:
        print(v["ShortName"], "-", v["Gender"])
    if not found:
        print("No voices start with", repr(prefix))


async def synthesize(text, out_path):
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH, volume=VOLUME)
    await communicate.save(out_path)


if LIST_VOICES:
    asyncio.run(list_voices(LIST_VOICES))
else:
    uploaded = files.upload()  # choose one or more .txt files
    for name in uploaded:
        with open(name, "r", encoding="utf-8-sig") as f:  # utf-8-sig also handles a BOM
            text = f.read().strip()
        if not text:
            print("Skipped (empty file):", name)
            continue
        out_file = os.path.splitext(name)[0] + ".mp3"
        asyncio.run(synthesize(text, out_file))
        print("Done ✅", out_file)
        files.download(out_file)
