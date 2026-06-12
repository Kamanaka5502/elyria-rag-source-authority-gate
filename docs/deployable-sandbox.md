# Deployable Sandbox

## Purpose

The deployable sandbox gives reviewers a simple way to run the public-safe RAG source authority engine against sample enterprise scenarios.

---

## Run Locally

From the repository root:

```bash
python sandbox/runner.py
```

The sandbox evaluates every JSON scenario in:

```text
examples/
```

It writes results to:

```text
sandbox/outputs/sandbox-results.json
```

---

## What the Sandbox Produces

Each result includes:

- scenario file
- scenario name
- expected outcome
- actual outcome
- reason codes
- required remediation

---

## Pilot Use

The sandbox can be used for:

- RAG governance workshops
- source authority reviews
- AI governance pilot reviews
- production-readiness conversations
- architecture interviews
- security and privacy review workshops

---

## Deployment Boundary

This sandbox is a reference implementation. Production deployment requires environment-specific security, identity, logging, privacy, legal, infrastructure, and policy review.
