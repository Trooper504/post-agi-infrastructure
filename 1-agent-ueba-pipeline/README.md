# Agent UEBA Pipeline

## Overview
This project is a local User and Entity Behavior Analytics (UEBA) pipeline for autonomous AI agents. It generates synthetic agent telemetry, trains an anomaly detector on the resulting behavior patterns, and exports the model to ONNX for lightweight local deployment.

## What It Does
* **`src/generate_logs.py`** creates synthetic execution logs for normal and rogue agent activity and saves them to `tests/synthetic_agent_logs.json`.
* **`src/train_model.py`** loads the synthetic logs, encodes the categorical fields, and trains an `IsolationForest` model to flag unusual behavior.
* **`src/export_onnx.py`** retrains the same model and exports it to `models/ueba_agent_model.onnx` for portable inference.

## Requirements
Use a local virtual environment for this folder and install the project dependencies from `requirements.txt`.

## Run the Pipeline
From the `1-agent-ueba-pipeline` directory, activate the environment in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Then run the scripts in order:

```powershell
python src/generate_logs.py
python src/train_model.py
python src/export_onnx.py
```

## Outputs
* Synthetic logs: `tests/synthetic_agent_logs.json`
* Exported model: `models/ueba_agent_model.onnx`

## Notes
* Run `generate_logs.py` before `train_model.py` or `export_onnx.py` so the input dataset exists.
* The scripts use relative paths rooted at `1-agent-ueba-pipeline`, so run them from that folder.