def calculate_pops(previous_ops, league_ops, park_factor, age_factor):
    """
    Calculate projected OPS (pOPS) using the provided formula.

    Args:
    - previous_ops (float): Player's previous OPS.
    - league_ops (float): League average OPS.
    - park_factor (float): Park factor.
    - age_factor (float): Age factor.

    Returns:
    - float: The projected OPS (pOPS).
    """
    pops = (4 * previous_ops / 3) + (league_ops / 3) + (park_factor / 3) + (age_factor / 3)-1
    return pops

# Example usage:
previous_ops = 0.829   # player's previous OPS
league_ops = 0.734     # league average OPS
park_factor = 1.05     # park factor
age_factor = 0.105      # age factor

pops = calculate_pops(previous_ops, league_ops, park_factor, age_factor)
print("Projected OPS (pOPS):", pops)