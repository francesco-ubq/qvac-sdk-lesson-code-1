#!/usr/bin/env bash
# Setup — the commands typed on screen
# Lesson: 1:19 (JavaScript) and 1:28 (Python)
set -euo pipefail

# JavaScript · Node 22 or newer
npm i @qvac/sdk

# Python ≥ 3.10
pip install tetherto-qvac-sdk

# once per machine
python -m tetherto.qvac_sdk install-worker
