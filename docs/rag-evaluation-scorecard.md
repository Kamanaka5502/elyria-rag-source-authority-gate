# RAG Evaluation Scorecard

## Purpose

The RAG Evaluation Scorecard provides a buyer-facing way to evaluate whether a RAG source or corpus is ready for pilot, production-candidate, or production use.

---

## Scoring Model

| Domain | Score | Notes |
|---|---:|---|
| Source approval | 0-5 | Is the source approved for the use case? |
| Source ownership | 0-5 | Is an accountable owner assigned? |
| Access authorization | 0-5 | Is retrieval access explicitly authorized? |
| Data classification | 0-5 | Is data classification documented? |
| Sensitivity controls | 0-5 | Are sensitive data controls present where required? |
| Freshness | 0-5 | Is the source current and lifecycle-managed? |
| Grounding readiness | 0-5 | Can output be traced to approved source evidence? |
| Telemetry | 0-5 | Can retrieval and output support be reconstructed? |
| Revalidation triggers | 0-5 | Are change conditions documented? |
| Production readiness | 0-5 | Are owners, controls, evidence, and review paths complete? |

Maximum score: 50

---

## Readiness Bands

| Score | Readiness Band | Decision Guidance |
|---:|---|---|
| 45-50 | Production-ready candidate | ADMIT if no critical blocker exists. |
| 35-44 | Pilot-ready with conditions | HOLD until gaps are resolved. |
| 20-34 | Not ready | HOLD / REFUSE depending on blockers. |
| 0-19 | High-risk / uncontrolled | REFUSE until source authority is rebuilt. |

---

## Critical Blockers

Any of the following should override the numeric score:

- source not approved
- access not authorized
- sensitive data controls missing
- source owner missing
- expired source
- grounding not validated for production use
- telemetry unavailable for required evidence

---

## Executive Summary Template

```text
This RAG source is currently [ADMIT / HOLD / REFUSE / REVALIDATE].
The primary readiness factors are [source authority, access scope, freshness, grounding, telemetry].
The required next steps are [remediation items].
```
