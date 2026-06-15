# Reasoning Data Recipes: Small Data, Open Data, and SFT/RL Synergy

A route for readers who care less about slogans and more about where the reasoning behavior actually comes from.

**Good for:** Students, reproduction builders, and open-source practitioners trying to assemble training data or starter pipelines.

**Why it is hot:** After DeepSeek-R1, many readers want recipes, not just model names: data filtering, distillation, SFT, and RL are the buy-in points.

## Reading Route

| Step | Paper | Why read it | Code |
|---:|---|---|---|
| 1 | [Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement](https://arxiv.org/abs/2409.12122) | Shows a modern open math model pipeline with self-improvement and math-centric training. | [Official](https://github.com/QwenLM/Qwen2.5-Math) |
| 2 | [LIMO: Less is More for Reasoning](https://arxiv.org/abs/2502.03387) | Argues that small but carefully selected reasoning data can unlock strong reasoning behavior. | [Official](https://github.com/GAIR-NLP/LIMO) / [Unofficial](https://github.com/StaryMoon/LIMO-Unofficial) |
| 3 | [OpenThoughts: Data Recipes for Reasoning Models](https://arxiv.org/abs/2506.04178) | A practical reference for open reasoning data construction, filtering, and recipe sharing. | [Official](https://github.com/open-thoughts/open-thoughts) |
| 4 | [AceReason-Nemotron: Advancing Math and Code Reasoning through SFT and RL Synergy](https://arxiv.org/abs/2505.16400) | Highlights the interaction between supervised reasoning data and RL for math/code performance. | - |
| 5 | [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) | A minimal and memorable reference for budget forcing and inference-time reasoning control. | [Official](https://github.com/simplescaling/s1) / [Unofficial](https://github.com/StaryMoon/s1-Test-Time-Scaling-Unofficial) |

## What to Compare

- Tiny curated data versus large open reasoning corpora.
- SFT-only unlocks versus RL-driven improvements.
- Math-only recipes versus math-plus-code recipes.

[Back to roadmap](../../README.md)
