# Post-AGI Infrastructure 

A suite of open-source, edge-resilient protocols designed for a reality where artificial general intelligence is a ubiquitous utility.

## The Premise

If we assume the major AI companies succeed—meaning that generalized intelligence becomes a nearly free commodity like electricity—the entire technological landscape flips. When AI can write standard code, analyze datasets, and build web apps instantly, those skills are no longer the bottleneck. 

***In my opininon*** the new bottlenecks will be **truth**, **local resilience**, **oversight**, and **data sovereignty**. 

This repository abandons the pursuit of building "more AI wrappers" and instead focuses on the infrastructure an AI-saturated world requires to remain stable.

## Architecture & Monorepo Structure

This repository is structured as a monorepo containing four strictly isolated, $0-cost local architectures. Each project maintains its own isolated virtual environment to prevent dependency collision.

### `1-agent-ueba-pipeline/` (AI Behavior Anomaly Detection)
As autonomous agents execute enterprise workflows, they will inevitably hallucinate, get stuck in infinite loops, or suffer prompt injections. This project treats agent execution logs as raw event data, utilizing an ONNX-compiled Isolation Forest to detect behavioral anomalies (UEBA) in real-time.

### `2-crypto-provenance/` (Hardware-to-Model Signing) *[Pending]*
In a world of hyper-realistic synthetic media, physical data must be verifiable the moment it is created. This pipeline cryptographically signs raw sensor telemetry before it touches a network, ensuring downstream systems can prove the data originated from the physical world.

### `3-edge-onnx-models/` (Offline Resilient Micro-Models) *[Pending]*
When society relies entirely on centralized AGI clouds, an internet outage is catastrophic. This framework compiles hyper-specialized small language models (SLMs) into INT8/INT4 ONNX graphs, allowing critical niche cultural knowledge to run entirely offline on standard CPU hardware.

### `4-ru-compliance-sandbox/` (Sovereign Routing Airgaps)
Major platforms constantly route telemetry across borders, violating strict national data localization laws. This FastAPI proxy intercepts AI data flows to mathematically guarantee compliance with local data sovereignty architectures, strictly air-gapping data from unverified external transit routes.

## Local Execution Environment

This entire monorepo is designed to execute locally on standard Windows hardware without requiring cloud GPUs or paid API keys.

**Global Requirements:**
* Python 3.10+
* Visual Studio Code

**Environment Management:**
Do not install dependencies globally. Navigate to the target project directory and activate its specific virtual environment before execution. For example, to run the UEBA pipeline:

    cd 1-agent-ueba-pipeline
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt

Repeat this activation pattern for `2-crypto-provenance`, `3-edge-onnx-models`, or `4-ru-compliance-sandbox` whenever working within those specific domains.
