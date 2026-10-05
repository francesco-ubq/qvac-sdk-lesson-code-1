# QVAC SDK quickstart — Python
# Lesson: 2:14 · card "quickstart.py"
#
# Same worker, same contract as the JavaScript client — but asyncio-native:
# open a Client in an `async with` block, pass client.transport to every call,
# and iterate run.events.
#
# Condensed from the official quickstart.py (https://docs.qvac.tether.io/, SDK v0.20.x).

from tetherto.qvac_sdk import (Client,
    completion, load_model, unload_model)
from tetherto.qvac_sdk.models import \
    LLAMA_3_2_1B_INST_Q4_0

async with Client() as client:
    t = client.transport
    model_id = await load_model(t,
        model_src=LLAMA_3_2_1B_INST_Q4_0)
    run = completion(t, model_id=model_id,
        history=[{'role': 'user', 'content': 'Hi!'}])
    async for event in run.events:
        if event.type == 'contentDelta':
            print(event.text, end='')
    await unload_model(t, model_id)
