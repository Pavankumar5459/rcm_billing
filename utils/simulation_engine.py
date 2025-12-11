import random

def simulate_access(eligibility, docs_ready, clinical_match):
    if not eligibility:
        return "Denied", "Eligibility"
    if not docs_ready:
        return "Denied", "Documentation"
    if not clinical_match:
        return "Denied", "Medical Necessity"
    return "Approved", "N/A"


def simulate_pa(documentation_score, severity):
    """Higher severity + lower documentation → higher denial chance."""
    base = 0.2 + (severity * 0.2) + (1 - documentation_score)
    approved = base < 0.5
    return "Approved" if approved else "Denied"


def simulate_claim(eligibility, pa_done, coding_score, documentation_score):
    if not eligibility:
        return "Denied", "Eligibility"
    if not pa_done:
        return "Denied", "Authorization"

    risk = (1 - coding_score) + (1 - documentation_score)

    if risk > 1:
        return "Denied", "Coding"

    return "Approved", "Clean Claim"
