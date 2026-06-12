# Grounding Readiness Model

## Purpose

Grounding readiness determines whether RAG output can be traced to approved, authorized, current, and relevant sources.

---

## Grounding Requirements

- approved source corpus
- access-scoped retrieval
- citation or evidence link
- current content status
- retrieval confidence review
- answer support check
- unsupported-answer handling
- refusal path for missing support

---

## Output Rules

```text
If the answer cannot be grounded, do not present it as supported.
If the source is not approved, do not retrieve it.
If the user lacks access, do not expose it.
If the source changed materially, revalidate it.
```

---

## Operating Principle

RAG quality is not only answer quality.

It is source authority, retrieval scope, grounding evidence, and lifecycle validity combined.
