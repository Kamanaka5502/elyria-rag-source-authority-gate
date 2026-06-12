# Expected RAG Source Outcomes

## Approved Policy Source

Input:

```text
examples/approved-policy-source.json
```

Expected outcome:

```text
ADMIT
```

Reason:

```text
Source approval, ownership, access, freshness, grounding, sensitivity controls, and telemetry are present.
```

---

## Stale Source With Unknown Owner

Input:

```text
examples/stale-unknown-owner-source.json
```

Expected outcome:

```text
HOLD
```

Reason:

```text
Source ownership and freshness must be resolved before retrieval supports enterprise output.
```

---

## Unauthorized Sensitive Source

Input:

```text
examples/unauthorized-sensitive-source.json
```

Expected outcome:

```text
REFUSE
```

Reason:

```text
The source is not approved, access is not authorized, and sensitive-data controls are missing.
```

---

## Changed Corpus Revalidation

Input:

```text
examples/changed-corpus-revalidation.json
```

Expected outcome:

```text
REVALIDATE
```

Reason:

```text
Prior approval cannot be relied on because the corpus changed.
```
