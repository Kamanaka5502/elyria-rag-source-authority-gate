# Sample RAG Source Authority Report

## Scenario

**Unauthorized Sensitive Source**

A RAG system is being evaluated for production-candidate use. The proposed source is support ticket history containing confidential customer information.

---

## Decision

```text
REFUSE
```

---

## Rationale

Retrieval cannot advance because the source is not approved, access is not authorized, and sensitive-data controls are missing.

---

## Evidence Summary

| Area | Status | Finding |
|---|---|---|
| Source type | Present | Support ticket history |
| Source owner | Present | Customer Support |
| Business owner | Present | Customer Operations |
| Technical owner | Present | AI Platform Team |
| Source approval | Missing | Source is not approved |
| Access authorization | Missing | Access is not authorized |
| Data classification | Confidential | Sensitive content is in scope |
| Sensitivity controls | Missing | Required controls are not present |
| Freshness | Current | Not the blocking issue |
| Grounding | Present | Not the blocking issue |
| Telemetry | Present | Not the blocking issue |

---

## Required Remediation

- Approve source before retrieval is allowed.
- Resolve identity and access scope.
- Implement sensitivity controls before retrieval.
- Re-run source authority review before pilot or production movement.

---

## Executive Summary

This RAG source should not advance to production-candidate use. The source may return for review after approval, access authorization, and sensitivity controls are resolved.
