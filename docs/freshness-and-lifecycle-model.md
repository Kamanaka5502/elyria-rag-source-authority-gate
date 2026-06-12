# Freshness and Lifecycle Model

## Purpose

RAG systems must know whether retrieved content is current enough for the decision, answer, recommendation, or workflow it supports.

---

## Freshness States

| State | Meaning | Default Decision |
|---|---|---|
| Current | Source is within approved lifecycle expectations. | ADMIT if other controls are present. |
| Unknown | Source age, owner, or update cadence is unclear. | HOLD |
| Stale | Source is outdated or not reviewed within required cadence. | HOLD |
| Expired | Source is no longer valid for operational use. | REFUSE |

---

## Lifecycle Questions

- Who owns the source?
- When was it last reviewed?
- What is the review cadence?
- What business process depends on it?
- What happens when it expires?
- Who approves refresh?
- Does retrieval require re-indexing after update?

---

## Revalidation Trigger

Any source update, corpus expansion, permission change, lifecycle expiration, policy change, model change, or prompt change should trigger revalidation.
