# Source Authority Model

## Purpose

The Source Authority Model defines how an enterprise determines whether a RAG system may retrieve from a source before AI output influences operational consequence.

---

## Core Question

```text
Is this source approved, owned, authorized, fresh, grounded, controlled, observable, and valid for the use case?
```

---

## Source Authority Layers

1. Source inventory
2. Source ownership
3. Business authority
4. Technical ownership
5. Access authorization
6. Sensitivity classification
7. Freshness and lifecycle status
8. Grounding and citation readiness
9. Retrieval telemetry
10. Revalidation triggers

---

## Source Classes

| Source Class | Example | Default Review Posture |
|---|---|---|
| Approved policy library | Compliance or HR policy source | ADMIT if current and access-scoped. |
| Knowledge base | Support or operations content | ADMIT / HOLD depending on freshness. |
| Wiki | Internal team documentation | HOLD unless ownership and freshness are clear. |
| Ticket history | Support, incidents, customer cases | HOLD / REFUSE depending on sensitivity. |
| Legal document set | Contracts, notices, legal guidance | REFUSE or escalate unless legal authority exists. |
| PDF repository | Mixed documents | HOLD until source authority and freshness are verified. |

---

## Operating Rule

```text
RAG retrieval is not source authority.
```

A system may be technically able to retrieve a document while still being unauthorized to use it for enterprise output.
