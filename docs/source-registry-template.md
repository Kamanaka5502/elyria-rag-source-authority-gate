# Source Registry Template

## Purpose

A source registry records which content sources a RAG system may retrieve from, who owns them, what data they contain, and whether they are approved for a specific use case.

---

## Registry Fields

| Field | Description |
|---|---|
| Source ID | Unique source identifier. |
| Source name | Human-readable source name. |
| Source type | Policy library, SharePoint site, wiki, knowledge base, PDF repository, ticket history, legal document set, data catalog. |
| Source owner | Accountable owner for the source. |
| Business owner | Owner of the use case relying on retrieval. |
| Technical owner | Owner of implementation and support. |
| Approved for RAG | Yes / No / Conditional. |
| Data classification | Public, internal, confidential, restricted, regulated. |
| Sensitive data | Yes / No. |
| Access model | Who may retrieve from this source. |
| Freshness status | Current, unknown, stale, expired. |
| Review cadence | How often the source is reviewed. |
| Grounding status | Whether source supports grounded output. |
| Telemetry required | Yes / No. |
| Revalidation triggers | Changes that force renewed review. |

---

## Example Entry

| Field | Example |
|---|---|
| Source ID | SRC-POLICY-001 |
| Source name | Approved Customer Support Policy Library |
| Source type | Policy library |
| Source owner | Policy Operations |
| Business owner | Compliance |
| Technical owner | AI Platform Team |
| Approved for RAG | Yes |
| Data classification | Internal |
| Sensitive data | No |
| Access model | Internal support staff only |
| Freshness status | Current |
| Review cadence | Quarterly |
| Grounding status | Grounding evaluation complete |
| Telemetry required | Yes |
| Revalidation triggers | Source update, corpus expansion, permission change, model change, prompt change, policy change |

---

## Registry Rule

```text
No source should enter a production RAG index unless ownership, approval, access, classification, freshness, grounding, telemetry, and revalidation conditions are documented.
```
