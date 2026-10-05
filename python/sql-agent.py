# Starter 3 of 3 — talk to your database (Python)
# Lesson: 5:12 · card "completion_tools pattern · run_sql is ours"
#
# A tool-calling agent: describe run_sql with a JSON schema, let the model pick
# the call, execute it yourself, append the result as a tool message and run
# completion again for a grounded answer.
#
# Open the database read-only — the model is writing your SQL.
#
# Condensed from the completion_tools.py pattern (https://docs.qvac.tether.io/); run_sql is ours.
#
# On-screen fragment. It runs inside the quickstart scaffold (an open Client,
# `t = client.transport`) and additionally needs `import sqlite3`, a `history`
# list and QWEN3_1_7B_INST_Q4. See python/quickstart.py.

TOOLS = [{'name': 'run_sql',
  'description': 'Run a read-only SQL query',
  'parameters': {'type': 'object',
    'properties': {'sql': {'type': 'string'}},
    'required': ['sql']}}]

db = sqlite3.connect('file:sales.db?mode=ro',
                     uri=True)

llm = await load_model(t, model_src=QWEN3_1_7B_INST_Q4,
    model_config={'ctx_size': 4096, 'tools': True})
run = completion(t, model_id=llm,
    history=history, tools=TOOLS)
final = await run.final

for call in final.tool_calls:
    rows = db.execute(call.arguments['sql']).fetchall()
    history.append({'role': 'tool', 'content': str(rows)})

answer = completion(t, model_id=llm,
    history=history, tools=TOOLS)
