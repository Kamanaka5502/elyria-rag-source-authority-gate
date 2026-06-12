# Architecture Diagram

## RAG Source Authority Flow

```mermaid
flowchart TD
    A[RAG Use Case Proposed] --> B[Source Inventory]
    B --> C[Source Owner Check]
    C --> D[Access Authorization]
    D --> E[Sensitivity Review]
    E --> F[Freshness and Lifecycle]
    F --> G[Grounding Readiness]
    G --> H[Retrieval Telemetry]
    H --> I{Decision}
    I -->|ADMIT| J[Retrieval May Proceed]
    I -->|HOLD| K[Complete Evidence]
    I -->|REFUSE| L[Block Retrieval]
    I -->|REVALIDATE| M[Run Source Review Again]
    J --> N[Monitor Retrieval]
    N --> O[Revalidation Triggers]
```

---

## Boundary Principle

```text
Retrieval access is not source authority.
```

A RAG system may be technically able to retrieve content while still being unauthorized to use it for enterprise output.
