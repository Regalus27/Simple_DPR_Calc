from DamageEvent import DamageEvent
from Utility import advantage_chance_recursive, validate_percentage

class Attack:
    def __init__(self, name: str, damage_events: list[DamageEvent], number_of_attacks=1, crit_chance=0.05, miss_chance=0.4, 
                 use_studied_attacks=False, studied_attacks_advantage_chance=0):
        if number_of_attacks < 0:
            self.number_of_attacks = 0
        else:
            self.number_of_attacks = number_of_attacks

        if self.number_of_attacks > 1:
            self.name = f'{name} (x{self.number_of_attacks}):'
        else:
            self.name = f'{name}:'
        
        self.damage_events = damage_events

        self.crit_chance = validate_percentage(crit_chance)
        self.miss_chance = validate_percentage(miss_chance)

        self.use_studied_attacks = use_studied_attacks
        self.studied_attacks_advantage_chance = validate_percentage(studied_attacks_advantage_chance)

    def calc_total_damage(self):
        if self.use_studied_attacks:
            return self.calc_studied_attacks_damage()
        return self.calc_normal_damage()

    """
    Calculate advantage crit and miss chances
    for each attack
        adv_chance * adv_damage + (1-adv_chance) * non_adv_damage
        pull up next advantage chance (for if another attack remains)
    """
    def calc_studied_attacks_damage(self):
        advantage_crit_chance = 1 - (1 - self.crit_chance) ** 2
        advantage_miss_chance = self.miss_chance ** 2

        total = 0

        for i in range(self.number_of_attacks):
            for damage_event in self.damage_events:
                advantage_damage = damage_event.calc_weighted_damage(advantage_crit_chance, advantage_miss_chance) * self.studied_attacks_advantage_chance
                normal_damage = damage_event.calc_weighted_damage(self.crit_chance, self.miss_chance) * (1 - self.studied_attacks_advantage_chance)
                total += advantage_damage + normal_damage
                
            self.studied_attacks_advantage_chance = advantage_chance_recursive(1, self.miss_chance, self.studied_attacks_advantage_chance)
        return total

    def calc_normal_damage(self):
        total = 0
        for damage_event in self.damage_events:
            total += damage_event.calc_weighted_damage(self.crit_chance, self.miss_chance)
        return total * self.number_of_attacks
    
    def display(self):
        result = ''
        result += f'{self.name:<42}{self.calc_total_damage():>5.2f} Average Attack Damage\n'
        for damage_event in self.damage_events:
            result += damage_event.display(self.crit_chance, self.miss_chance) + '\n'
        return result