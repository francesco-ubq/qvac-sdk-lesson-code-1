// loadModel({ modelSrc }) — the three model sources
// Lesson: 1:42 · card "modelSrc: three sources"
//
// loadModel downloads, caches and hands back a modelId, whichever source you give it.
//
// `…` is the elision shown on screen — see the docs for the full URL form.

// 1. registry constant
modelSrc: LLAMA_3_2_1B_INST_Q4_0
// 2. Hugging Face / HTTP URL
modelSrc: 'https://huggingface.co/…/model.gguf'
// 3. local file
modelSrc: './models/my-model.gguf'
