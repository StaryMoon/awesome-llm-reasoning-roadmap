# Verifiers, Process Rewards, and Self-Judging Models

A route for understanding why final-answer accuracy is not enough and why step-level reward became central.

**Good for:** Readers interested in PRMs, reward modeling, math verification, and scalable supervision.

**Why it is hot:** Reasoning RL needs reward signals; process supervision is one of the main ways to make those rewards less sparse.

## Reading Route

| Step | Paper | Why read it | Code |
|---:|---|---|---|
| 1 | [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168) | Early demonstration that verifier-guided selection can improve mathematical reasoning outputs. | - |
| 2 | [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | Popularized process supervision for mathematical reasoning, not just final-answer supervision. | - |
| 3 | [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://arxiv.org/abs/2309.12284) | Shows the importance of data bootstrapping and question rewriting for math reasoning. | [Official](https://github.com/meta-math/MetaMath) |
| 4 | [MATH-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations](https://arxiv.org/abs/2312.08935) | Builds step-level supervision without dense human annotations, linking verification to scalable reward construction. | [Official](https://github.com/peiyi9979/math-shepherd) |
| 5 | [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) | Explores using the model itself as a judge, a key motif in scalable preference and reward pipelines. | - |

## What to Compare

- Outcome supervision versus process supervision.
- Human annotations versus synthetic or model-generated step labels.
- External verifiers versus self-judging models.

[Back to roadmap](../../README.md)
