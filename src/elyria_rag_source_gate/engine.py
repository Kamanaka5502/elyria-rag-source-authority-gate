"""Public-safe reference engine for RAG source authority evaluation.

This module demonstrates how enterprise RAG source scenarios can be classified
into ADMIT, HOLD, REFUSE, or REVALIDATE outcomes using explicit source,
access, freshness, grounding, telemetry, and revalidation evidence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class SourceDecision:
    outcome: str
    reason_codes: List[str] = field(default_factory=list)
    required_remediation: List[str] = field(default_factory=list)
    evidence: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "outcome": self.outcome,
            "reason_codes": self.reason_codes,
            "required_remediation": self.required_remediation,
            "evidence": self.evidence,
        }


def present(value: Any) -> bool:
    return value is not None and value != "" and value is not False


def evaluate_rag_source(scenario: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate a RAG source authority scenario."""

    if scenario.get("revalidation_required") is True:
        return SourceDecision(
            outcome="REVALIDATE",
            reason_codes=["REVALIDATION_REQUIRED"],
            required_remediation=["Re-run source authority review before retrieval proceeds."],
            evidence=scenario,
        ).to_dict()

    hold_reasons: List[str] = []
    hold_fix: List[str] = []

    for field_name, fix in [
        ("source_owner", "Assign a source owner."),
        ("business_owner", "Assign a business owner."),
        ("technical_owner", "Assign a technical owner."),
    ]:
        if not present(scenario.get(field_name)):
            hold_reasons.append(f"MISSING_{field_name.upper()}")
            hold_fix.append(fix)

    if scenario.get("freshness_status") in {"unknown", "stale"}:
        hold_reasons.append("FRESHNESS_NOT_VALIDATED")
        hold_fix.append("Validate source freshness and lifecycle status.")

    if scenario.get("grounding_evaluation") is not True:
        hold_reasons.append("GROUNDING_NOT_VALIDATED")
        hold_fix.append("Complete grounding and citation readiness review.")

    refuse_reasons: List[str] = []
    refuse_fix: List[str] = []

    if scenario.get("source_approved") is not True:
        refuse_reasons.append("SOURCE_NOT_APPROVED")
        refuse_fix.append("Approve source before retrieval is allowed.")

    if scenario.get("access_authorized") is not True:
        refuse_reasons.append("ACCESS_NOT_AUTHORIZED")
        refuse_fix.append("Resolve identity and access scope before retrieval.")

    if scenario.get("sensitive_data") is True and scenario.get("sensitivity_controls") is not True:
        refuse_reasons.append("SENSITIVE_DATA_CONTROLS_MISSING")
        refuse_fix.append("Implement sensitivity controls before retrieval.")

    if refuse_reasons:
        return SourceDecision("REFUSE", refuse_reasons, refuse_fix, scenario).to_dict()

    if hold_reasons:
        return SourceDecision("HOLD", hold_reasons, hold_fix, scenario).to_dict()

    if scenario.get("telemetry_required") is True and scenario.get("telemetry_present") is not True:
        return SourceDecision(
            outcome="HOLD",
            reason_codes=["RETRIEVAL_TELEMETRY_MISSING"],
            required_remediation=["Implement retrieval telemetry before production use."],
            evidence=scenario,
        ).to_dict()

    return SourceDecision(
        outcome="ADMIT",
        reason_codes=["SOURCE_AUTHORITY_RESOLVED"],
        required_remediation=[],
        evidence=scenario,
    ).to_dict()
