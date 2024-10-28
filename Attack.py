from DamageEvent import DamageEvent

class Attack:
    def __init__(self, name: str, damage_events: list[DamageEvent], number_of_attacks=1, crit_chance=0.05, miss_chance=0.4):
        self.name = name + ':'

        if number_of_attacks < 0:
            self.number_of_attacks = 0
        else:
            self.number_of_attacks = number_of_attacks
        
        self.damage_events = damage_events

        self.crit_chance = crit_chance
        self.miss_chance = miss_chance

    def calc_total_damage(self):
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
    
    def modify_crit(self, new_crit_chance=0.05, new_miss_chance=0.4):
        """
        Used to modify critical strike chance partway through a round, if that somehow happens.
        """
        self.crit_chance = new_crit_chance
        self.miss_chance = new_miss_chance