def calc_dice_average(dice_quantity: int, dice_value: int):
    if dice_quantity <= 0:
        return 0
    
    if dice_value <= 0:
        return 0

    return dice_quantity * (dice_value / 2 + 0.5)

def validate_level(level: int):
    if level < 1:
        return 1
    if level > 20:
        return 20
    return level