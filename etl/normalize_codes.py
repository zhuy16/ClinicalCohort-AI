from __future__ import annotations

from typing import Optional

# Code prefixes — customize per dataset as needed
# These are examples from a diabetes/CKD dataset; other datasets may use different codes
DIABETES_CODES_PREFIX = "E11"  # Example: ICD-10 Type 2 Diabetes
CKD_CODES_PREFIX = "N18"       # Example: ICD-10 Chronic Kidney Disease

# LOINC codes — examples
HBA1C_LOINC = "4548-4"         # Example: HbA1c
EGFR_LOINC = "33914-3"         # Example: eGFR
CREATININE_LOINC = "2160-0"    # Example: Creatinine

# Drug mappings — customize per dataset
# Current example: SGLT2 inhibitors; adapt to your domain
SGLT2_RXNORM = {
    "2200644": "empagliflozin",
    "1545149": "canagliflozin",
    "1488574": "dapagliflozin",
}

SGLT2_NAME_TO_RXNORM = {v: k for k, v in SGLT2_RXNORM.items()}


def normalize_icd10(code: Optional[str]) -> Optional[str]:
    """Normalize ICD-10 codes (standardize format and casing)."""
    if code is None:
        return None
    cleaned = code.strip().upper()
    if not cleaned:
        return None
    return cleaned


def normalize_loinc(code: Optional[str]) -> Optional[str]:
    """Normalize LOINC codes."""
    if code is None:
        return None
    cleaned = code.strip()
    return cleaned if cleaned else None


def normalize_rxnorm(rxnorm_code: Optional[str], drug_name: Optional[str]) -> Optional[str]:
    """Normalize RxNorm codes (standardize format)."""
    if rxnorm_code:
        return rxnorm_code.strip()
    if not drug_name:
        return None
    return SGLT2_NAME_TO_RXNORM.get(drug_name.lower().strip())


def condition_bucket(icd10_code: Optional[str]) -> str:
    """
    Map ICD-10 code to a disease category.
    Customize this for your dataset's domain of interest.
    """
    if not icd10_code:
        return "unknown"
    if icd10_code.startswith(DIABETES_CODES_PREFIX):
        return "diabetes"
    if icd10_code.startswith(CKD_CODES_PREFIX):
        return "ckd"
    return "other"
