def calculate_pera(previous_era, league_era, park_factor, defense_factor, age_factor):
    """
    Calculate projected ERA (pERA) using the provided formula.

    Args:
    - previous_era (float): Player's previous ERA.
    - league_era (float): League average ERA.
    - park_factor (float): Park factor.
    - defense_factor (float): Defense factor.
    - age_factor (float): Age factor.

    Returns:
    - float: The projected ERA (pERA).
    """
    pera = (4 * previous_era / 3) + (league_era / 3) + (park_factor / 3) - (defense_factor / 3) + (age_factor / 3)
    return pera

# Example usage:
previous_era = 2.86  # player's previous ERA
league_era = 3.93     # league average ERA
park_factor = .5   # park factor
defense_factor = 7.25  # defense factor
age_factor = 1.05      # age factor

pera = calculate_pera(previous_era, league_era, park_factor, defense_factor, age_factor)
print("Projected ERA (pERA):", pera)