# Project title (working)
When does suspend-and-resume pay off for I/O-bound AI agents?

## Research questions
RQ1: What fraction of an agent's wall-clock time is spent waiting?
RQ2: How much compute cost does hibernation save compared with always-on and async-multiplexed baselines?
RQ3: What latency overhead does resume add (p50/p95/p99), and where is the break-even point?
RQ4: What are the cold-start and memory overheads of Wasm, microVM and container sandboxes for agent-generated code?

## Hypotheses
H1: ...
H2: ...

## In scope
- Prototype controller, Redis state store, mock LLM/tool servers, sandbox comparison, cost model

## Out of scope (for now)
- Long-term vector-database memory
- Large-scale real LLM usage (we use mocks)

## Success criteria
- Measured results for all four RQs with repeated runs and confidence intervals