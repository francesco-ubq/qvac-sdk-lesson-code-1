// Swap the task. Keep the shape.
// Lesson: 2:02 · card "same shape: ({ modelId, … })"
//
// One contract across every capability: pass the modelId, get a run back.
//
// `…` is the elision shown on screen — see the docs for each task's own arguments.

completion({ modelId, history })
embed({ modelId, text })
transcribe({ modelId, audioChunk })
translate({ modelId, text, … })
textToSpeech({ modelId, text })
