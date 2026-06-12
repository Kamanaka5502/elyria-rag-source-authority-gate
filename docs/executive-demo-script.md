# Executive Demo Script

## Purpose

This script supports a concise buyer, hiring-panel, or executive walkthrough of the Elyria RAG Source Authority Gate.

---

## Opening

```text
This repository addresses a critical enterprise AI problem: RAG systems can retrieve content before the organization has proven whether the source is approved, current, owned, access-scoped, grounded, and safe to use.

The question is not only whether the system can retrieve a document. The question is whether the system is allowed to trust it, cite it, expose it, and use it before output influences enterprise consequence.
```

---

## Walkthrough Path

1. Start with `README.md` and explain the retrieval-trust problem.
2. Open `docs/source-authority-model.md` and show source authority layers.
3. Open `docs/access-scope-and-sensitivity.md` and show access/sensitivity boundaries.
4. Open `docs/freshness-and-lifecycle-model.md` and show freshness states.
5. Open `docs/grounding-readiness-model.md` and show grounding requirements.
6. Open `sandbox/runner.py` and explain the local sandbox.
7. Open `reports/sample-rag-source-authority-report.md` and show the enterprise output.

---

## Close

```text
The value is controlled retrieval. This gives enterprises a repeatable pattern for deciding which sources can be used, which require more evidence, which must be refused, and which must be revalidated before AI output becomes operational consequence.
```
