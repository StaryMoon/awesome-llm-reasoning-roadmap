# Reasoning RL Systems: GRPO, Long-CoT, and Open Reasoners

The route that connects DeepSeekMath, DeepSeek-R1, Kimi k1.5, DAPO, ORZ, and Skywork-OR1.

**Good for:** LLM researchers tracking modern RL recipes for math, code, and long-chain reasoning.

**Why it is hot:** This is the current high-traffic cluster: reasoning ability as an RL-trained behavior rather than only a prompt trick.

## Reading Route

| Step | Paper | Why read it | Code |
|---:|---|---|---|
| 1 | [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) | Introduced GRPO in a math reasoning setting and set up much of the later DeepSeek-R1 storyline. | [Official](https://github.com/deepseek-ai/DeepSeek-Math) |
| 2 | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | The central public reference for RL-driven long-chain reasoning and distillation into smaller models. | [Official](https://github.com/deepseek-ai/DeepSeek-R1) / [Unofficial](https://github.com/StaryMoon/DeepSeek-R1-Unofficial) |
| 3 | [Kimi k1.5: Scaling Reinforcement Learning with LLMs](https://arxiv.org/abs/2501.12599) | Connects long-context RL and reasoning scaling, useful for comparing with DeepSeek-R1. | [Unofficial](https://github.com/StaryMoon/Kimi-k1-5-Unofficial) |
| 4 | [QwQ-32B: Embracing the Power of Reinforcement Learning](https://qwenlm.github.io/blog/qwq-32b/) | A widely discussed open reasoning model release that makes RL-centered reasoning visible to builders. | [Official](https://github.com/QwenLM/Qwen) |
| 5 | [Llama-Nemotron: Efficient Reasoning Models](https://arxiv.org/abs/2505.00949) | A strong industrial open reasoning family, useful for comparing distillation and efficiency-focused recipes. | [Official](https://github.com/NVIDIA/NeMo) |
| 6 | [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476) | A systems-oriented RL recipe for large-scale reasoning training. | [Unofficial](https://github.com/StaryMoon/DAPO-Unofficial) |
| 7 | [Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model](https://arxiv.org/abs/2503.24290) | Pushes open RL-on-base-model training for reasoning, useful for reproducibility-minded readers. | [Unofficial](https://github.com/StaryMoon/Open-Reasoner-Zero-Unofficial) |
| 8 | [Skywork Open Reasoner 1 Technical Report](https://arxiv.org/abs/2505.22312) | A recent open-reasoner report focused on long-CoT math and code reasoning. | [Unofficial](https://github.com/StaryMoon/Skywork-OR1-Unofficial) |

## What to Compare

- Which parts are SFT, RL, rejection sampling, distillation, or verifier-driven selection.
- How each system defines rewards for math/code correctness.
- How much of the recipe depends on base model quality versus RL infrastructure.

[Back to roadmap](../../README.md)
