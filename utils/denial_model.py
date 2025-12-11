import numpy as np
import random

def predict_denial(cpt_complexity, documentation_score, eligibility_ok, pa_done):
    """Predicts denial probability & category based on rules."""

    # Base denial probability from CPT complexity
    base_rate = 0.05 + (cpt_complexity * 0.10)

    # Documentation reduces denials
    doc_factor = (1 - documentation_score)

    # Eligibility issues override everything
    if not eligibility_ok:
        return 0.95, "Eligibility"

    # Missing PA is a major cause
    if not pa_done:
        return 0.65, "Authorization"

    final_rate = base_rate + doc_factor
    final_rate = min(final_rate, 0.95)

    categories = ["Coding", "Medical Necessity", "Authorization"]
    return final_rate, random.choice(categories)
