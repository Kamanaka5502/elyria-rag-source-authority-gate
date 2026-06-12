# Production Readiness Checklist

## Purpose

This checklist defines what must be resolved before a RAG source or corpus is allowed to support pilot, production-candidate, or production AI output.

---

## Ownership

- [ ] Business owner assigned
- [ ] Technical owner assigned
- [ ] Source owner assigned
- [ ] Data owner assigned where required
- [ ] Security reviewer assigned where required
- [ ] Privacy reviewer assigned where required

---

## Source Authority

- [ ] Source inventory completed
- [ ] Source approved
- [ ] Source purpose documented
- [ ] Source owner identified
- [ ] Source lifecycle documented
- [ ] Source review cadence documented

---

## Access and Sensitivity

- [ ] User access model defined
- [ ] Application identity defined
- [ ] Retrieval permissions mapped
- [ ] Data classification documented
- [ ] Sensitive data status confirmed
- [ ] Sensitivity controls implemented where required

---

## Freshness and Grounding

- [ ] Freshness status confirmed
- [ ] Expired content excluded
- [ ] Grounding evaluation completed
- [ ] Unsupported-answer behavior defined
- [ ] Citation or evidence expectations defined

---

## Telemetry

- [ ] Retrieval event captured
- [ ] Source ID captured
- [ ] Source owner captured
- [ ] Access decision captured
- [ ] Data classification captured
- [ ] Grounding result captured
- [ ] Decision outcome captured
- [ ] Reason codes captured

---

## Final Production Decision

```text
ADMIT      Source authority is resolved.
HOLD       Evidence, ownership, freshness, or grounding remains incomplete.
REFUSE     Source approval, access, or sensitivity boundary is missing.
REVALIDATE Conditions changed; prior approval is stale.
```
