# Deployment Modes

## Mode 1: Local Sandbox

Run sample scenarios locally:

```bash
python sandbox/runner.py
```

Use this mode for portfolio review, buyer education, and hiring-panel demonstration.

---

## Mode 2: Workshop Demo

Use the README, source authority model, grounding model, and sample report in a guided RAG governance discussion.

---

## Mode 3: Pilot Readiness Review

Use the checklist, scenarios, and sandbox outputs to evaluate whether a RAG source or corpus can support pilot or production-candidate use.

---

## Mode 4: Enterprise Adaptation

Adapt the public-safe reference model to a specific environment.

Required additions:

- identity and access integration
- source registry integration
- vector index governance
- retrieval logging
- data classification policy
- freshness lifecycle automation
- grounding evaluation method
- incident and revalidation path

---

## Mode 5: Production Control Pattern

Production use requires environment-specific implementation and validation.

This public repository should be treated as a reference architecture and pilot sandbox, not as a complete production enforcement system.
