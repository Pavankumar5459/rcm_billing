import pandas as pd

def calculate_allowed_amount(cpt, locality, fee_schedule, geo_data):
    """Returns allowed amount using CMS fee schedule * locality adjustment."""

    try:
        base_rate = fee_schedule.loc[fee_schedule["hcpcs_code"] == cpt, "allowed_amount"]
        if base_rate.empty:
            return None

        base_rate = float(base_rate.values[0])

        loc_factor = geo_data.loc[geo_data["locality"] == locality, "gcpi"]
        loc_factor = float(loc_factor.values[0]) if not loc_factor.empty else 1.0

        return round(base_rate * loc_factor, 2)

    except:
        return None
