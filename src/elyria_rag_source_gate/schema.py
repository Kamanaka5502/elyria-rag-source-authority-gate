"""Scenario schema helpers for the public-safe RAG source authority engine."""

REQUIRED_FIELDS = [
    "scenario",
    "stage",
    "source_type",
    "source_approved",
    "source_owner",
    "business_owner",
    "technical_owner",
    "access_authorized",
    "data_classification",
    "sensitive_data",
    "sensitivity_controls",
    "freshness_status",
    "grounding_evaluation",
    "telemetry_required",
    "telemetry_present",
    "revalidation_required",
]

DECISIONS = ["ADMIT", "HOLD", "REFUSE", "REVALIDATE"]

SOURCE_TYPES = [
    "policy_library",
    "sharepoint_site",
    "knowledge_base",
    "support_ticket_history",
    "legal_document_set",
    "pdf_repository",
    "wiki",
    "data_catalog",
]

FRESHNESS_STATUS = ["current", "unknown", "stale", "expired"]
