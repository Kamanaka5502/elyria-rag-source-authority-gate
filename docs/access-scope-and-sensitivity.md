# Access Scope and Sensitivity

## Purpose

RAG governance requires more than approved documents. It requires proof that the requester, application, agent, or workflow is allowed to retrieve and use the content in context.

---

## Access Questions

- Who is requesting retrieval?
- What identity is the RAG system using?
- What source is being queried?
- What content class may be returned?
- Is the data internal, confidential, regulated, or public?
- Does the output expose content to unauthorized users?
- Is sensitive data minimized or filtered?
- Is downstream use allowed?

---

## Sensitivity Boundary

| Data Classification | Default Posture |
|---|---|
| Public | ADMIT if source is approved and fresh. |
| Internal | ADMIT / HOLD depending on ownership and grounding. |
| Confidential | HOLD unless access and sensitivity controls are explicit. |
| Restricted / Regulated | REFUSE unless separate governance authorizes retrieval. |

---

## Operating Principle

Source permission and user permission must both be resolved.

A source may be approved for one group, workflow, or use case and still be prohibited for another.
