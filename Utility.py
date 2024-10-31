"""
Studied Attacks (Fighter 13)
This returns the chance for an attack to have advantage based on the chance that the previous attack had advantage.
This took me hours to figure out so I really hope it works.
f(0) = 0
f(x) = ((1 - f(x - 1)) * miss_chance) + (f(x - 1) * miss_chance ** 2)

I should make this a proper recursive function
(loops_remaining, miss_chance, last_chance=0)
chance = ((1 - last_chance) * miss_chance) + (last_chance * miss_chance**2)
if loops_remaining > 0:
    return advantage_chance_recursive(loops_remaining - 1, miss_chance, last_chance=chance)
return chance
"""
def advantage_chance_recursive(attacks_made: int, miss_chance=0.4, last_chance=0):
    chance = last_chance
    if attacks_made > 0:
        chance = ((1 - last_chance) * miss_chance) + (last_chance * miss_chance**2)
        return advantage_chance_recursive(attacks_made - 1, miss_chance, last_chance=chance)
    return chance

def calc_dice_average(dice_quantity: int, dice_value: int):
    if dice_quantity <= 0:
        return 0
    
    if dice_value <= 0:
        return 0

    return dice_quantity * (dice_value / 2 + 0.5)

def get_proficiency_mod(level: int):
    mod = 0
    match level:
        case level if level >= 1 and level <= 4:
            mod = 2
        case level if level >= 5 and level <= 8:
            mod = 3
        case level if level >= 9 and level <= 12:
            mod = 4
        case level if level >= 13 and level <= 16:
            mod = 5
        case level if level >= 17 and level <= 20:
            mod = 6
        case _:
            mod = 0
    return mod

def get_stat_mod(level: int):
    """
    Assumes +3 level 1, +4 level 4, +5 level 8+
    """
    mod = 0
    match level:
        case level if level >= 1 and level <= 3:
            mod = 3
        case level if level >= 4 and level <= 7:
            mod = 4
        case level if level >= 8 and level <= 20:
            mod = 5
        case _:
            mod = 0
    return mod

"""
Chance to have landed a critical strike this turn for the purposes of Great Weapon Master, getting an extra attack as a bonus action
"""
def great_weapon_master_attack_chance(number_of_attacks: int, miss_chance=0.4, crit_chance=0.05, studied_attacks=False, initial_advantage_chance=0):
    if number_of_attacks < 1:
        return 0
    if not studied_attacks:
        return 1 - (1 - crit_chance) ** number_of_attacks
    # If studied attacks
    cumulative_chance = 1
    for i in range(1, number_of_attacks + 1):
        # Calculate weighted crit chance w/ no advantage chance
        no_advantage_crit_chance = (1 - initial_advantage_chance) * crit_chance
        # Calculate weighted crit chance w/ advantage chance
        advantage_crit_chance = initial_advantage_chance * (1 - (1 - crit_chance) ** 2)
        # Update the chance to not crit w/ each attack
        cumulative_chance *= 1 - (advantage_crit_chance + no_advantage_crit_chance)
        # Update initial advantage chance, as it is now going to be used to store the previous advantage chance
        initial_advantage_chance = advantage_chance_recursive(i, miss_chance=miss_chance, last_chance=initial_advantage_chance)
    # Reverse to get cumulative chance to have crit
    cumulative_chance = 1 - cumulative_chance
    return cumulative_chance

def validate_level(level: int):
    if level < 1:
        return 1
    if level > 20:
        return 20
    return level

def validate_percentage(percentage: float):
    if percentage < 0:
        return 0
    if percentage > 1:
        return 1
    return percentage