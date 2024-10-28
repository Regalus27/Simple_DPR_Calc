from Attack import Attack

class Round:
    """
    Round tracks all attacks that the character will make in a given round.
    Populated by a Combat object

    If I wanted to be crazy I could track Action / Bonus Action spending
    But Action Surge would complicate that
    """
    def __init__(self, round_number: int, attacks: list[Attack], level: int):
        self.attacks = attacks
        
        if level < 1:
            self.level = 1
        elif level > 20:
            self.level = 20
        else:
            self.level = level

        self.round_number = round_number
        
    def calc_round_damage(self):
        total = 0
        for attack in self.attacks:
            total += attack.calc_total_damage()
        return total
    
    def display(self):
        result = f'Level {self.level}, Round {self.round_number}:'
        result = f'{result:<42}{self.calc_round_damage():>5.2f} Average Round Damage\n'
        for attack in self.attacks:
            result += attack.display() + '\n'
        return result