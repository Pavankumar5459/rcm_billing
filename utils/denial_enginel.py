def classify_denial(reason_text: str):
    """
    Simple NLP-style rule engine for denial reasons.
    """

    r = reason_text.lower()

    if any(x in r for x in ["auth", "authorization", "pa", "prior"]):
        return "Authorization Denial"

    if any(x in r for x in ["eligibility", "coverage", "benefit"]):
        return "Eligibility / Coverage Denial"

    if any(x in r for x in ["coding", "cpt", "modifier", "hcpcs"]):
        return "Coding Error"

    if any(x in r for x in ["timely", "late"]):
        return "Timely Filing"

    if any(x in r for x in ["medical necessity", "not medically", "records"]):
        return "Medical Necessity"

    return "Other"


def denial_appeal_recommendation(denial_type):
    """
    Returns recommended actions for providers.
    """

    mapping = {
        "Authorization Denial": "Submit missing clinical notes + retrospective PA request.",
        "Eligibility / Coverage Denial": "Verify active coverage; submit corrected claim.",
        "Coding Error": "Review CPT/HCPCS, modifiers; submit corrected claim.",
        "Timely Filing": "Request reconsideration with proof-of-attempt.",
        "Medical Necessity": "Attach medical records + provider attestation.",
        "Other": "Review payer correspondence for additional detail."
    }

    return mapping.get(denial_type, "Review payer documentation.")
