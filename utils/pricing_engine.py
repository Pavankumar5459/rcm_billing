def calculate_patient_oop(allowed, deductible_remaining=0, coinsurance_rate=0.2):
    """
    Calculates patient out-of-pocket using:
    - Allowed amount
    - Remaining deductible
    - Coinsurance %
    """

    allowed = float(allowed)

    # Apply deductible
    deductible_applied = min(allowed, deductible_remaining)
    remaining_after_deductible = allowed - deductible_applied

    # Coinsurance applies to the remaining
    coinsurance = remaining_after_deductible * coinsurance_rate

    # Patient pays deductible + coinsurance
    patient_pay = deductible_applied + coinsurance

    # Payer pays the rest
    payer_pay = allowed - patient_pay

    return {
        "allowed_amount": round(allowed, 2),
        "deductible_applied": round(deductible_applied, 2),
        "coinsurance": round(coinsurance, 2),
        "patient_responsibility": round(patient_pay, 2),
        "payer_payment": round(payer_pay, 2),
    }
