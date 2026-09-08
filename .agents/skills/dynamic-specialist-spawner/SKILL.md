---
name: dynamic-specialist-spawner
description: >-
  Use this skill whenever a problem domain exceeds the core council's immediate focus
  (e.g., Graph Neural Networks, Causal Inference, Reinforcement Learning, Speech/Audio, Robotics),
  requiring an on-demand specialist to be instantiated and dissolved after task resolution.
---

# Dynamic Specialist Spawner (Tier 0 Core Skill)

To avoid cognitive bloat and agent proliferation, niche domains are not modeled as permanent council members. Instead, the Orchestrator instantiates dynamic specialists on demand.

## 1. Trigger Conditions

Spawn a Dynamic Specialist when a query requires deep, non-standard domain specialization:
- **Causal Inference Specialist:** Doubly robust estimation, instrumental variables, do-calculus, synthetic controls.
- **Graph ML Specialist:** GCN, GAT, GraphSAGE, message passing, spectral graph theory, heterophilic graphs.
- **Reinforcement Learning Specialist:** MDP formulation, policy gradients (PPO, SAC), value iteration, Q-learning, RLHF/DPO.
- **Speech & Audio Specialist:** Spectrograms, CTC loss, Mel-Frequency Cepstral Coefficients, conformers, vocoders.
- **Computer Vision Specialist:** Spatial attention, vision transformers (ViT), object detection architectures, segmentation.

## 2. Instantiation Protocol

1. Formulate the specialist's concise mandate, expertise scope, and constraints.
2. Bind the relevant Tier 1 or Tier 2 skills and reference tools.
3. Consult the specialist alongside relevant core council members (e.g., ML Architect + Graph ML Specialist).
4. Synthesize the findings through the Orchestrator.
5. Record key insights into Research and Decision memory, then gracefully dissolve the temporary specialist session.
