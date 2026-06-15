# Start Here: CoT to Self-Consistency

A compact route for understanding why reasoning traces became a first-class interface for LLMs.

**Good for:** Students and engineers who want the shortest path from prompting to modern reasoning terminology.

**Why it is hot:** Almost every recent reasoning paper still uses CoT, self-consistency, and decomposition as its baseline vocabulary.

## Reading Route

| Step | Paper | Why read it | Code |
|---:|---|---|---|
| 1 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) | The canonical paper that made intermediate natural-language reasoning traces a standard interface. | - |
| 2 | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) | Shows that sampling multiple reasoning paths and marginalizing answers can beat greedy CoT. | - |
| 3 | [Least-to-Most Prompting Enables Complex Reasoning in Large Language Models](https://arxiv.org/abs/2205.10625) | Turns hard reasoning into a sequence of easier subproblems, making decomposition an explicit strategy. | - |
| 4 | [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) | Bootstraps rationales from the model itself, foreshadowing self-improvement loops for reasoning. | [Official](https://github.com/ezelikman/STaR) |
| 5 | [Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking](https://arxiv.org/abs/2403.09629) | Extends latent/internal rationale ideas by training models to generate useful intermediate thoughts. | [Official](https://github.com/ezelikman/quiet-star) |

## What to Compare

- Whether reasoning is produced only at inference time or also used for training.
- Whether the method improves reasoning by better prompts, better sampling, or better data.
- Whether rationales are treated as explanations, latent computation, or supervision signals.

[Back to roadmap](../../README.md)
