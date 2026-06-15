# Agents, Tools, and Executable Reasoning

A route through reasoning systems that leave pure text and interact with tools, code, memory, and environments.

**Good for:** Agent builders, tool-use researchers, and people interested in executable reasoning traces.

**Why it is hot:** Tool-use and agent workflows are where reasoning becomes visible as actions instead of only text.

## Reading Route

| Step | Paper | Why read it | Code |
|---:|---|---|---|
| 1 | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | Connects reasoning traces with actions, observations, and tool-like environments. | [Official](https://github.com/ysymyth/ReAct) |
| 2 | [Program-Aided Language Models](https://arxiv.org/abs/2211.10435) | Uses programs as executable reasoning traces, separating symbolic execution from language generation. | [Official](https://github.com/reasoning-machines/pal) |
| 3 | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | Self-supervises tool-use decisions, a precursor to tool-augmented reasoning systems. | - |
| 4 | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | Adds verbal feedback and episodic memory to language agents for iterative improvement. | [Official](https://github.com/noahshinn/reflexion) |
| 5 | [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | Frames reasoning improvement as generate-feedback-revise without external labels. | [Official](https://github.com/madaan/self-refine) |
| 6 | [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://arxiv.org/abs/2309.17452) | Combines tool-integrated trajectories with math reasoning, bridging CoT and executable agents. | [Official](https://github.com/microsoft/ToRA) |
| 7 | [Scaling Test-Time Compute for LLM Agents](https://arxiv.org/abs/2506.12928) | Extends test-time scaling from single prompts to agent loops, tool calls, and multi-step workflows. | - |
| 8 | [Scaling Test-Time Compute Optimally in LLM Agentic Coding](https://arxiv.org/abs/2604.16529) | A timely bridge between coding agents and inference-time compute allocation. | - |

## What to Compare

- Whether tools are called through prompting, fine-tuning, or self-supervised API annotations.
- Whether the system learns from environment feedback, self-feedback, or external execution.
- Whether the reasoning trace is natural language, code, or action-observation memory.

[Back to roadmap](../../README.md)
