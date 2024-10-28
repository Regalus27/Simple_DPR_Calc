from DiceUtility import calc_dice_average

class DamageEvent:
    def __init__(self, dice_quantity, dice_value, flat_value, name="Unknown Source",
                 can_crit=True, conditional_chance=1, always_hit=False,
                 damage_on_miss=0):
        self.name = name + ':'

        if dice_quantity < 0:
            self.dice_quantity = 0
        else:
            self.dice_quantity = dice_quantity

        if dice_value < 0:
            self.dice_value = 0
        else:
            self.dice_value = dice_value
        
        self.flat_value = flat_value
        self.can_crit = can_crit

        if conditional_chance > 1:
            self.conditional_chance = 1
        elif conditional_chance < 0:
            self.conditional_chance = 0
        else:
            self.conditional_chance = conditional_chance

        self.always_hit = always_hit

        if damage_on_miss < 0:
            self.damage_on_miss = 0
        else:
            self.damage_on_miss = damage_on_miss
    
    def calc_critical_damage(self):
        """
        Returns average damage of a critical strike
        Will be multiplied by critical strike chance later for DPR calcs
        """
        # If this damage event cannot crit, return the damage of a normal attack.
        if not self.can_crit:
            return self.calc_hit_damage()
        
        dice_damage = (calc_dice_average(self.dice_quantity, self.dice_value)) * 2
        flat_damage = self.flat_value
        
        return (dice_damage + flat_damage) * self.conditional_chance

    def calc_hit_damage(self):
        """
        Returns average damage of a non-critical strike
        """
        dice_damage = calc_dice_average(self.dice_quantity, self.dice_value)
        flat_damage = self.flat_value

        return (dice_damage + flat_damage) * self.conditional_chance

    def calc_miss_damage(self):
        """
        Returns average damage of a missed strike - usually 0
        """
        if not self.always_hit:
            # Apply miss damage if this damage can miss
            return self.damage_on_miss * self.conditional_chance
        
        return self.calc_hit_damage()
    
    def calc_weighted_damage(self, crit_chance, miss_chance):
        hit_chance = 1 - crit_chance - miss_chance

        if crit_chance < 0 or crit_chance > 1:
            crit_chance = 0
        if hit_chance < 0 or hit_chance > 1:
            hit_chance = 0
        if miss_chance < 0 or miss_chance > 1:
            miss_chance = 0

        return (crit_chance * self.calc_critical_damage()) + (hit_chance * self.calc_hit_damage()) + (miss_chance * self.calc_miss_damage())
    
    def display(self, crit_chance=0.05, miss_chance=0.4):
        """
        Returns a string reading XdX + X, X Average Damage, X% Conditional Chance
        """
        average_damage = self.calc_weighted_damage(crit_chance, miss_chance)
        
        # Formatting
        conditional = f'{self.conditional_chance:2.0%}'
        return f'{self.name:<30}{self.dice_quantity:>2}d{self.dice_value:<2} + {self.flat_value:>2}, {average_damage:>5.2f} Average Damage, {conditional:>4} Conditional Chance'
        