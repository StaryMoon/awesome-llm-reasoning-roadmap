# Benchmarks and Stress Tests: Code, Browsing, Expert Exams, and Robustness

A route for checking whether a reasoning claim survives outside the paper's favorite setting.

**Good for:** Readers who want to evaluate reasoning models, write reproduction reports, or avoid benchmark theater.

**Why it is hot:** Hard benchmarks and robustness tests are what turn reasoning hype into something comparable.

## Reading Route

| Step | Paper | Why read it | Code |
|---:|---|---|---|
| 1 | [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://arxiv.org/abs/2403.07974) | A high-traffic code reasoning benchmark designed to reduce contamination and track evolving coding ability. | [Official](https://github.com/LiveCodeBench/LiveCodeBench) |
| 2 | [Humanity's Last Exam](https://arxiv.org/abs/2501.14249) | A viral hard benchmark for frontier models, useful for tracking whether reasoning claims survive expert-level questions. | [Official](https://github.com/centerforaisafety/hle) |
| 3 | [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516) | Makes web-browsing and information-seeking reasoning a concrete evaluation target. | - |
| 4 | [Robust Reasoning Benchmark: Assessing LLMs' Mathematical Reasoning Capabilities Against Natural Input Perturbations](https://arxiv.org/abs/2602.09838) | Moves beyond headline math accuracy by probing whether reasoning is stable under natural perturbations. | - |
| 5 | [Does More Inference-Time Compute Really Help Robust Reasoning?](https://arxiv.org/abs/2604.10739) | A useful counterweight to hype: more thinking can be brittle, wasteful, or even harmful under some perturbations. | - |

## What to Compare

- Static benchmark accuracy versus live or contamination-resistant evaluation.
- Math and code reasoning versus browsing-agent reasoning.
- Higher test-time compute versus robustness under perturbation.

[Back to roadmap](../../README.md)
