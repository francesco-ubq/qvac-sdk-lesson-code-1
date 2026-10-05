// QVAC SDK quickstart — JavaScript
// Lesson: 1:55 · card "quickstart.js"
//
// Load a model, stream a completion, unload. Every task in the SDK has the
// same four beats: load → run → unload → close.
//
// Condensed from the official quickstart.js (https://docs.qvac.tether.io/, SDK v0.20.x);
// the progress callback and try/catch were dropped so the shape stays visible.

import { loadModel, completion, unloadModel,
  LLAMA_3_2_1B_INST_Q4_0 } from '@qvac/sdk'

const modelId = await loadModel({
  modelSrc: LLAMA_3_2_1B_INST_Q4_0 })

const run = completion({ modelId, stream: true,
  history: [{ role: 'user', content: 'Hi!' }] })
for await (const token of run.tokenStream)
  process.stdout.write(token)

await unloadModel({ modelId })
