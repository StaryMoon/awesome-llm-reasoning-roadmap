# Deliberate Search: Trees, Graphs, and Test-Time Compute

A route through explicit search over thoughts and the newer idea that inference-time compute is itself a scaling axis.

**Good for:** Readers interested in budget forcing, inference-time search, and non-greedy reasoning.

**Why it is hot:** Test-time scaling is one of the clearest bridges between old reasoning prompts and current reasoning models.

## Reading Route

| Step | Paper | Why read it | Code |
|---:|---|---|---|
| 1 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) | Turns reasoning into explicit search over intermediate thought states. | [Official](https://github.com/princeton-nlp/tree-of-thought-llm) |
| 2 | [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687) | Generalizes thought structures from chains and trees to graph-like transformations. | [Official](https://github.com/spcl/graph-of-thoughts) |
| 3 | [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) | Frames inference-time compute as a scaling axis, setting the stage for budget forcing and search-like inference. | - |
| 4 | [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) | A minimal and memorable reference for budget forcing and inference-time reasoning control. | [Official](https://github.com/simplescaling/s1) / [Unofficial](https://github.com/StaryMoon/s1-Test-Time-Scaling-Unofficial) |
| 5 | [LIMO: Less is More for Reasoning](https://arxiv.org/abs/2502.03387) | Argues that small but carefully selected reasoning data can unlock strong reasoning behavior. | [Official](https://github.com/GAIR-NLP/LIMO) / [Unofficial](https://github.com/StaryMoon/LIMO-Unofficial) |
| 6 | [A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?](https://arxiv.org/abs/2503.24235) | A convenient entry point for readers trying to organize search, self-refinement, verification, and budget control. | - |
| 7 | [The Art of Scaling Test-Time Compute for LLMs](https://arxiv.org/abs/2512.02008) | Organizes practical decisions around when and how to spend extra inference compute. | - |
| 8 | [Does More Inference-Time Compute Really Help Robust Reasoning?](https://arxiv.org/abs/2604.10739) | A useful counterweight to hype: more thinking can be brittle, wasteful, or even harmful under some perturbations. | - |

## What to Compare

- How the search state is represented: chain, tree, graph, or budget-controlled continuation.
- Whether additional compute is spent on sampling, search, verification, or longer thinking.
- How much performance comes from inference strategy versus training data.

[Back to roadmap](../../README.md)
