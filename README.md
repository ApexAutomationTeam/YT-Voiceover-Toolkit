# YT Voiceover Toolkit

**Free tools for YouTube creators: turn a script into a natural voiceover, and pull vocals or music out of an audio track.**

This repo packages a ready-to-run **Google Colab notebook** for neural text-to-speech (Urdu, Hindi, English and more) with `edge-tts`, plus notes on two free companion tools: **Ultimate Vocal Remover** for extracting audio/music, and **Piper** for browser-based text-to-speech.

> Built by [Apex Automation Team](https://apexautomationteam.com/). See real automation builds running on the **[Sample Works page](https://apexautomationteam.com/sample-works/)**.

---

## At a glance

| | |
|---|---|
| **Type** | Google Colab notebook / Python script + tool guide |
| **Runs in** | Google Colab (free tier works), nothing to install locally |
| **Language** | Python 3 |
| **Dependencies** | `edge-tts`, `nest_asyncio` (installed by the notebook) |
| **Input** | One or more `.txt` files |
| **Output** | `.mp3` voiceover per file, downloaded automatically |
| **Controls** | Voice, speed (`RATE`), pitch (`PITCH`), volume (`VOLUME`) |

## What's inside

```
yt-voiceover-toolkit/
├── notebooks/edge_tts_colab.ipynb   Colab notebook (recommended)
├── scripts/edge_tts_colab.py        same code as a plain script / paste-able cell
└── README.md
```

---

## 1. Text to speech in Google Colab (edge-tts)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-username>/<repo-name>/blob/main/notebooks/edge_tts_colab.ipynb)

1. Open the notebook in Colab (badge above, or upload `edge_tts_colab.ipynb` at [colab.research.google.com](https://colab.research.google.com/)).
2. Run the first cell (`!pip install -q edge-tts nest_asyncio`).
3. In the second cell, set `VOICE` (see the table below) and optionally `RATE`, `PITCH`, `VOLUME`.
4. Run the cell, choose your `.txt` file(s) in the upload dialog.
5. The `.mp3` is created and downloaded automatically. Several files in one go are supported.

### Settings

| Setting | Default | Meaning |
|---|---|---|
| `VOICE` | `en-US-GuyNeural` | Which neural voice reads the text |
| `RATE` | `+0%` | Speed, for example `-10%` slower or `+15%` faster |
| `PITCH` | `+0Hz` | For example `-2Hz` deeper or `+3Hz` higher |
| `VOLUME` | `+0%` | Loudness adjustment |
| `LIST_VOICES` | `None` | Set to a prefix such as `"ur-"` or `"hi-"` to print the available voices instead of making audio |

### Voices

| Language | Voice | Gender | Note |
|---|---|---|---|
| Urdu | `ur-PK-AsadNeural` | Male | Best male Urdu option in our notes |
| Urdu | `ur-PK-UzmaNeural` | Female | |
| Hindi | `hi-IN-MadhurNeural` | Male | Deep voice |
| Hindi | `hi-IN-SwaraNeural` | Female | |
| English (US) | `en-US-GuyNeural` | Male | Notebook default |
| English (US) | `en-US-DavisNeural` | Male | |
| English (US) | `en-US-AriaNeural` | Female | |

**Quick rule**

- Urdu script text (اردو) -> `ur-PK-*`
- Roman Urdu (Urdu written in English letters) -> `hi-IN-*` (our notes recommend this; try a short sample first)
- Mixed Urdu/English -> `en-US-*`

Voice availability can change. To see what exists right now, set `LIST_VOICES = "ur-"` (or `"hi-"`, `"en-US"`) and run the cell.

### What the notebook handles

- Several files per run; each gets its own `.mp3`, named after the text file.
- Files that are not `.txt` are converted safely (the original is never overwritten).
- Empty files are skipped with a message; a UTF-8 byte-order mark is ignored.
- Works inside Colab's already-running event loop (`nest_asyncio`).

---

## 2. Extract audio / music: Ultimate Vocal Remover (UVR)

[Ultimate Vocal Remover GUI v5.6](https://github.com/Anjok07/ultimatevocalremovergui/releases/tag/v5.6) is a free, open-source (MIT) desktop app that uses neural models to **split a track into vocals and instrumental**. Typical uses for video work: get a clean instrumental or background music bed, or isolate a voice.

- Windows 10 or newer, plus macOS builds, from the release page. Follow the installer notes on the release page (they recommend installing to the main `C:` drive on Windows).
- A GPU helps for speed. The release page lists separate builds for AMD / Intel graphics.
- Add your audio file, pick a separation model, choose an output folder and start processing.

Only process audio you own or have the right to use.

## 3. Browser text to speech: Piper

[Piper TTS tool](https://piper.ttstool.com/) runs the open-source Piper neural voices in your browser. It is quick and needs no account, and it is a good fit for **English**. For **Urdu it is not the best option**; use the `ur-PK` voices from section 1 instead.

---

## Suggested workflow for a voiceover video

1. Write the script as a `.txt` file (one language per file works best).
2. Generate the voiceover with the Colab notebook; adjust `RATE` and `PITCH` until it sounds right.
3. If you need a music bed from an existing track, extract the instrumental with UVR.
4. Combine voice and music in your video editor and balance the levels.

## Known limitations

- `edge-tts` is an unofficial client for Microsoft Edge's online read-aloud service. It needs an internet connection, is not an official Microsoft product and can change or break without notice.
- Very long scripts take longer; split them into several `.txt` files if a run times out.
- Pronunciation of names, numbers and mixed-language text varies by voice. Listen to a short sample before generating a full script.
- Roman Urdu is read by a Hindi voice, so some words may sound slightly different from native Urdu.

## Responsible use

Check the terms that apply to the voices and tools you use, especially before using generated audio commercially or monetizing a channel. Follow YouTube's policies on synthetic or altered content, including any disclosure rules that apply, and do not use voices to mislead people or imitate real individuals without permission.

## Maintenance & support

Online services change. If the notebook stops working, a voice disappears or you get an error, email **[contact@apexautomationteam.com](mailto:contact@apexautomationteam.com)** with the error message and the voice you used, and we will look into it.

## Need a custom tool?

We build automation, scrapers, QA and back-office systems to your exact spec and keep them updated. Tell us what you need at **[contact@apexautomationteam.com](mailto:contact@apexautomationteam.com)**, visit **[Apex Automation Team](https://apexautomationteam.com/)** or see more builds on the **[Sample Works page](https://apexautomationteam.com/sample-works/)**.

## License

Add your preferred license (for example MIT) before publishing.
