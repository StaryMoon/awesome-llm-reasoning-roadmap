# Contributing

Contributions are welcome. This repository is a focused roadmap for LLM reasoning papers, so entries should be relevant to at least one of these themes:

- chain-of-thought and rationale learning;
- decomposition, search, and test-time scaling;
- tool use, agents, and executable reasoning;
- verifiers, process reward models, and self-judging systems;
- reasoning RL, long-CoT, and open reasoner training;
- frontier reports with explicit reasoning modes or math/code reasoning emphasis.

Good contributions:

- add a missing paper to `data/papers.json`;
- add or correct official code links;
- add a StaryMoon unofficial reproduction link when available;
- improve reading tracks in `data/tracks.json`;
- improve generated visuals, tables, or the searchable HTML page.

After editing data files, run:

```bash
python scripts/build.py
python scripts/build.py --check
python -m json.tool data/papers.json
python -m json.tool data/tracks.json
```

Please do not copy paper figures or tables into this repository unless the license explicitly permits redistribution.
