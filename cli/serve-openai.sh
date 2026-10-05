#!/usr/bin/env bash
# qvac serve --openai — your laptop as an OpenAI-compatible endpoint
# Lesson: 2:25 · terminal card "CLI · npm i -g @qvac/cli"
#
# Point your existing tools at http://localhost:11434/v1/ — no cloud, no keys.
#
# `…` is the elision shown on screen; fill in a model id and your messages.
set -euo pipefail

npm i -g @qvac/cli
qvac serve --openai

curl localhost:11434/v1/chat/completions \
  -d '{"model":"…","messages":[…]}'
