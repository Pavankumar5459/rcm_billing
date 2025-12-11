def simulate_access(coverage_score, auth_required, network_status):
    """
    Estimates likelihood of patient access success.
    """

    score = coverage_score

    if auth_required:
        score -= 15

    if network_status == "OON":
        score -= 25

    if score < 0:
        score = 0
    if score > 100:
        score = 100

    return round(score, 2)


def simulate_prior_auth(complexity, documentation_quality):
    """
    Simulates PA approval probability based on:
    - Medical necessity strength
    - Documentation completeness
    """

    base_rate = 70 - (complexity * 5)
    doc_bonus = documentation_quality * 3

    rate = base_rate + doc_bonus
    return max(0, min(100, rate))


def simulate_claim(payment_accuracy, coding_quality, auth_status):
    """
    Predict adjudication outcome.
    """

    score = payment_accuracy + coding_quality

    if auth_status == "Missing":
        score -= 40

    if score > 120:
        return "Paid"
    elif score > 80:
        return "Partially Paid"
    else:
        return "Denied"
