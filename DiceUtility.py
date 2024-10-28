def calc_dice_average(dice_quantity, dice_value):
    if dice_quantity <= 0:
        return 0
    
    if dice_value <= 0:
        return 0

    return dice_quantity * (dice_value / 2 + 0.5)