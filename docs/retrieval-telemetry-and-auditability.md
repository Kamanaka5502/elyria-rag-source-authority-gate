# Retrieval Telemetry and Auditability

## Purpose

RAG governance requires evidence of what was retrieved, why it was retrieved, who requested it, what authority allowed it, and whether output was grounded.

---

## Required Evidence

| Evidence | Purpose |
|---|---|
| Request ID | Tie retrieval to a specific event. |
| User or workflow identity | Identify who or what initiated retrieval. |
| Source ID | Identify the approved source. |
| Source owner | Preserve accountability. |
| Access decision | Prove retrieval was authorized. |
| Data classification | Show sensitivity level. |
| Freshness status | Show whether source was current. |
| Retrieved passages | Preserve retrieval trace where appropriate. |
| Grounding result | Show whether output was supported. |
| Decision outcome | ADMIT / HOLD / REFUSE / REVALIDATE. |
| Reason codes | Explain the decision. |

---

## Audit Questions

- What source was queried?
- Was the source approved?
- Who owns the source?
- Was access authorized?
- Was sensitive data in scope?
- Was the content current?
- Was the output grounded?
- What decision was made?
- What evidence supports that decision?
- What changed after approval?

---

## Operating Principle

If retrieval cannot be reconstructed, RAG governance cannot be proven.
