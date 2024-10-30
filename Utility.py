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