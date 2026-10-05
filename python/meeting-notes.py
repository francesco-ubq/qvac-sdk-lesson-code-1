# Starter 2 of 3 — meeting notes that never leave the room (Python)
# Lesson: 4:36 · card "tetherto-qvac-sdk · transcribe + completion"
#
# Transcribe the recording with Whisper Tiny, unload it, then ask a small LLM
# for the action items. Each streamed response carries a segment with start and
# end in milliseconds.
#
# Need to know who said what? Parakeet Sortformer does speaker diarization (5:02).
#
# Condensed from transcription.py + quickstart.py (https://docs.qvac.tether.io/).
#
# On-screen fragment. It assumes the quickstart imports plus transcribe and the
# TranscribeRequest model, WHISPER_TINY and QWEN3_1_7B_INST_Q4. The exact import
# paths are in the SDK docs; python/quickstart.py has the surrounding scaffold.

async with Client() as client:
    t = client.transport
    whisper = await load_model(t, model_src=WHISPER_TINY,
        model_config={'audio_format': 'f32le',
                      'language': 'en'})
    req = TranscribeRequest.model_validate({
        'type': 'transcribe', 'modelId': whisper,
        'audioChunk': {'type': 'filePath',
                       'value': 'standup.wav'},
        'metadata': True})
    segs = [r.segment async for r in transcribe(t, req)
            if r.segment is not None]
    text = ''.join(s.text for s in segs)
    await unload_model(t, whisper)

    llm = await load_model(t, model_src=QWEN3_1_7B_INST_Q4)
    run = completion(t, model_id=llm, history=[{
        'role': 'user',
        'content': f'Action items:\n{text}'}])
    async for ev in run.events:
        if ev.type == 'contentDelta':
            print(ev.text, end='')
