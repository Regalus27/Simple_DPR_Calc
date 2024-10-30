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