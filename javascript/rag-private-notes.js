// Starter 1 of 3 — chat with your private notes (JavaScript)
// Lesson: 3:59 · card "@qvac/sdk · rag + completion"
//
// Embed your documents into a workspace, retrieve the top chunks at question
// time, then put them in the system prompt and stream the answer.
//
// The built-in vector store is for prototypes. In production keep embed() and
// plug in SQLite, Mongo or LanceDB instead (lesson 4:19).
//
// Condensed from rag-managed.js + quickstart.js (https://docs.qvac.tether.io/).
//
// On-screen fragment. It assumes the quickstart imports plus the RAG helpers:
//   import { loadModel, completion, unloadModel, ragIngest, ragSearch,
//     GTE_LARGE_FP16, LLAMA_3_2_1B_INST_Q4_0 } from '@qvac/sdk'
// and `myNotes` / `query` from your own app. See javascript/quickstart.js.

const embedId = await loadModel({
  modelSrc: GTE_LARGE_FP16 })
await ragIngest({ modelId: embedId,
  workspace: 'notes', documents: myNotes })

const hits = await ragSearch({ modelId: embedId,
  workspace: 'notes', query, topK: 3 })
const context = hits.map(h => h.content).join('\n')

const llmId = await loadModel({
  modelSrc: LLAMA_3_2_1B_INST_Q4_0 })
const run = completion({ modelId: llmId, stream: true,
  history: [
    { role: 'system', content: `Answer from:\n${context}` },
    { role: 'user', content: query }] })
for await (const t of run.tokenStream)
  process.stdout.write(t)
