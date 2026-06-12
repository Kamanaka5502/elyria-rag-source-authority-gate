<div align="center">

# Elyria RAG Source Authority Gate

## RAG Governance · Source Authority · Grounding Readiness · Retrieval Control

<img src="assets/rag-source-authority-gate.jpg" alt="Elyria RAG Source Authority Gate" width="100%">

![License](https://img.shields.io/badge/license-MIT-1f4f5a?style=for-the-badge)
![RAG Governance](https://img.shields.io/badge/RAG%20Governance-Source%20Authority-1f4f5a?style=for-the-badge)
![Grounding](https://img.shields.io/badge/Grounding-Readiness%20Gate-2f6f73?style=for-the-badge)
![Access Scope](https://img.shields.io/badge/Access%20Scope-Authorized%20Retrieval-c9a66b?style=for-the-badge)
![Deployable Sandbox](https://img.shields.io/badge/Deployable-Sandbox%20Runner-5f8fa3?style=for-the-badge)
![Executive Ready](https://img.shields.io/badge/Executive--Ready-Board%20Readable-c9a66b?style=for-the-badge)

### **Govern what an AI system may retrieve, trust, cite, and use before output becomes enterprise consequence.**

![Sources](https://img.shields.io/badge/Sources-Approved%20%7C%20Owned%20%7C%20Fresh-2f6f73?style=flat-square)
![Decision](https://img.shields.io/badge/Decision-ADMIT%20%7C%20HOLD%20%7C%20REFUSE%20%7C%20REVALIDATE-1f4f5a?style=flat-square)
![Telemetry](https://img.shields.io/badge/Telemetry-Retrieval%20Evidence-5f8fa3?style=flat-square)
![Pilot Ready](https://img.shields.io/badge/Pilot--Ready-Source%20Trust%20Review-c9a66b?style=flat-square)

</div>

---

## Executive Signal

```text
RAG retrieval is not source authority.
```

A system may be technically able to retrieve a document while still being unauthorized to use it for enterprise output.

The Elyria RAG Source Authority Gate turns retrieval from a hidden implementation detail into an explicit enterprise governance boundary.

---

## Repository Navigation

| Area | Start Here | Outcome |
|---|---|---|
| Executive overview | `README.md` | Understand the retrieval-trust problem and business value. |
| Source authority | `docs/source-authority-model.md` | Determine whether a source is approved, owned, and valid. |
| Access and sensitivity | `docs/access-scope-and-sensitivity.md` | Resolve identity, access, data classification, and sensitivity controls. |
| Freshness lifecycle | `docs/freshness-and-lifecycle-model.md` | Check whether source content is current enough for operational use. |
| Grounding readiness | `docs/grounding-readiness-model.md` | Determine whether output can be traced to approved sources. |
| Retrieval evidence | `docs/retrieval-telemetry-and-auditability.md` | Define what must be logged to prove governed retrieval. |
| Pilot sandbox | `docs/deployable-sandbox.md` and `sandbox/runner.py` | Execute example scenarios locally. |
| Sample output | `reports/sample-rag-source-authority-report.md` | Review an enterprise-style readiness report. |

---

## Deployable Sandbox Quick Start

Run the public-safe sandbox from the repository root:

```bash
python sandbox/runner.py
```

The sandbox evaluates every RAG source scenario in:

```text
examples/
```

It produces decision results at:

```text
sandbox/outputs/sandbox-results.json
```

Expected path:

```text
approved-policy-source.json          → ADMIT
stale-unknown-owner-source.json      → HOLD
unauthorized-sensitive-source.json   → REFUSE
changed-corpus-revalidation.json     → REVALIDATE
```

---

## What This Solves

RAG systems are not safe because they retrieve documents.

They are safe only when the enterprise can prove which sources are approved, who owns them, whether access is authorized, whether content is fresh, whether retrieval is grounded, whether sensitive data is controlled, and whether output can be trusted before it influences operational consequence.

Companies are connecting AI systems to SharePoint, wikis, PDFs, support articles, ticket histories, legal documents, policy libraries, data catalogs, and internal repositories without a consistent way to prove source authority, freshness, access scope, grounding quality, telemetry, and revalidation.

The **Elyria RAG Source Authority Gate** provides a public-safe, enterprise-ready reference architecture for governing retrieval-augmented generation before AI output becomes enterprise action, advice, compliance position, customer response, or internal decision support.

---

## Why Enterprises Benefit

Enterprise teams gain a repeatable way to convert RAG risk into operational architecture:

- approved source registry
- source ownership model
- access and sensitivity boundary
- freshness and lifecycle review
- grounding readiness review
- citation and evidence expectations
- retrieval telemetry requirements
- production readiness checklist
- revalidation after source, corpus, permission, prompt, model, policy, or environment change

The business value is direct: safer RAG deployment, stronger source trust, reduced hallucination exposure, clearer data governance, stronger auditability, and faster production-readiness review.

---

## Decision Model

```text
ADMIT      Retrieval may proceed from approved, authorized, fresh, grounded sources.
HOLD       Source evidence, ownership, freshness, or grounding is incomplete.
REFUSE     Retrieval cannot proceed because source authority or access boundary is missing.
REVALIDATE Source, corpus, permission, freshness, model, prompt, or policy changed.
```

---

## Enterprise Architecture Flow

```text
RAG use case proposed
        ↓
Source inventory
        ↓
Source owner and authority check
        ↓
Access scope and sensitivity review
        ↓
Freshness and lifecycle review
        ↓
Grounding and citation readiness
        ↓
Telemetry and evidence requirements
        ↓
ADMIT / HOLD / REFUSE / REVALIDATE
        ↓
Retrieval only if governed
        ↓
Monitoring, drift, and revalidation
```

---

## Decision Signal Palette

| Signal | Meaning | Enterprise Use |
|---|---|---|
| **ADMIT** | Source authority is resolved. | Retrieval can support the approved use case. |
| **HOLD** | Evidence is incomplete. | Ownership, freshness, grounding, or telemetry must be completed. |
| **REFUSE** | Source or access boundary is missing. | Retrieval must not proceed. |
| **REVALIDATE** | Prior approval is stale. | Source, corpus, permission, prompt, model, or policy changed. |

---

## End-to-End Coverage

| Layer | Enterprise Question | Repository Asset |
|---|---|---|
| Source authority | Which sources may the AI system retrieve from? | `docs/source-authority-model.md` |
| Access scope | Who may retrieve what content through the RAG system? | `docs/access-scope-and-sensitivity.md` |
| Freshness | Is the content current enough for operational use? | `docs/freshness-and-lifecycle-model.md` |
| Grounding | Can output be traced to approved sources? | `docs/grounding-readiness-model.md` |
| Telemetry | What evidence proves what was retrieved and why? | `docs/retrieval-telemetry-and-auditability.md` |
| Production readiness | What must be resolved before pilot or production movement? | `docs/production-readiness-checklist.md` |
| Deployable sandbox | How can sample scenarios be executed locally? | `docs/deployable-sandbox.md` and `sandbox/runner.py` |
| Sample report | What does an enterprise-ready RAG review output look like? | `reports/sample-rag-source-authority-report.md` |
| Architecture diagram | How does the source gate move from intake to decision? | `docs/architecture-diagram.md` |

---

## Public-Safe Components

| Asset | Purpose |
|---|---|
| `src/elyria_rag_source_gate/engine.py` | Public-safe decision engine for ADMIT / HOLD / REFUSE / REVALIDATE. |
| `src/elyria_rag_source_gate/schema.py` | Scenario schema helpers and decision constants. |
| `sandbox/runner.py` | Local sandbox runner for example RAG source scenarios. |
| `docs/source-authority-model.md` | Core model for approved, owned, authorized sources. |
| `docs/access-scope-and-sensitivity.md` | Access, identity, and sensitive data boundary model. |
| `docs/freshness-and-lifecycle-model.md` | Source freshness, lifecycle, and expiration model. |
| `docs/grounding-readiness-model.md` | Grounding, citation, and retrieval confidence model. |
| `docs/retrieval-telemetry-and-auditability.md` | Evidence requirements for retrieval and output support. |
| `docs/production-readiness-checklist.md` | Enterprise deployment readiness checklist. |
| `docs/deployable-sandbox.md` | Sandbox runbook and pilot usage documentation. |
| `docs/deployment-modes.md` | Local, workshop, pilot, enterprise, and production adaptation modes. |
| `docs/architecture-diagram.md` | Mermaid architecture diagram. |
| `examples/*.json` | Public-safe RAG source authority scenarios. |
| `reports/sample-rag-source-authority-report.md` | Example enterprise readiness report. |
| `tests/expected-rag-source-outcomes.md` | Public-safe expected outcomes. |
| `NOTICE.md` | Public-safe boundary and attribution notice. |

---

## Relationship to the Elyria Enterprise AI Governance Suite

```text
Elyria Enterprise AI Control Plane
= governs enterprise AI movement across the organization.

Elyria Agent Action Boundary
= governs tool-using agents that may touch systems, data, workflows, communications, or operational action.

Elyria RAG Source Authority Gate
= governs retrieval trust: what knowledge AI may retrieve, trust, cite, and use.
```

This repository is the retrieval-trust layer of the suite.

---

## Public Boundary

This repository is public-safe. It demonstrates architecture surfaces, sandbox logic, examples, and enterprise readiness models, not private Elyria Systems runtime machinery, protected validators, customer-specific builds, commercial proof-corridor internals, credentials, keys, or confidential implementation details.

**Show the architecture. Protect the machinery.**
