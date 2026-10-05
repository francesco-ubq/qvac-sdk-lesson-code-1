# QVAC SDK lesson — code from the video

Every code card shown in the QVAC SDK lesson, one file per snippet, in the order
it appears. The lesson builds with [QVAC](https://qvac.tether.io/), Tether's
open-source local-first AI SDK: text, embeddings and RAG, transcription,
translation, TTS, OCR and vision, all running on your own device.

Docs: <https://docs.qvac.tether.io/> · Examples: <https://github.com/tetherto/qvac>

## Files

| Time | File | What it shows |
| --- | --- | --- |
| 1:19 / 1:28 | [`cli/install.sh`](cli/install.sh) | `npm i @qvac/sdk` (Node ≥ 22), `pip install tetherto-qvac-sdk`, install the worker once |
| 1:42 | [`javascript/model-sources.js`](javascript/model-sources.js) | `loadModel({ modelSrc })` — registry constant, Hugging Face URL, or a local `.gguf` |
| 1:55 | [`javascript/quickstart.js`](javascript/quickstart.js) | load → stream a completion → unload |
| 2:02 | [`javascript/same-shape.js`](javascript/same-shape.js) | swap the task, keep the shape |
| 2:14 | [`python/quickstart.py`](python/quickstart.py) | the same contract, asyncio-native |
| 2:25 | [`cli/serve-openai.sh`](cli/serve-openai.sh) | `qvac serve --openai` — an OpenAI-compatible endpoint on localhost |
| 2:45 | [`sql/top-customers.sql`](sql/top-customers.sql) | the query the agent writes |
| 3:59 | [`javascript/rag-private-notes.js`](javascript/rag-private-notes.js) | **Starter 1** — chat with your private notes (RAG) |
| 4:36 | [`python/meeting-notes.py`](python/meeting-notes.py) | **Starter 2** — meeting notes that never leave the room |
| 5:12 | [`python/sql-agent.py`](python/sql-agent.py) | **Starter 3** — talk to your database (tool calling) |

## About these files

They are the snippets **as they appear on screen**, transcribed verbatim so you
can pause the video and follow along. That means two things:

- They are condensed from the official examples in the QVAC SDK docs (v0.20.x) —
  progress callbacks, `try`/`catch` and error handling were dropped to keep the
  shape readable at video size.
- The three starter files are fragments, not whole programs. Each one says at the
  top what it assumes (imports, an open `Client`, your own data). The two
  quickstart files are complete and are the scaffold the fragments drop into.
- A `…` in the code is the elision shown on screen, not valid syntax. The docs
  have the full form.

Check the current docs before copying into production — this is a snapshot of
SDK v0.20.x as taught in the lesson.
