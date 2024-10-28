from Attack import Attack

class Round:
    """
    Round tracks all attacks that the character will make in a given round.
    """
    def __init__(self, round_number: int, attacks: list[Attack], round_description=''):
        self.attacks = attacks
        self.description = round_description

        self.round_number = validate_round_number(round_number)
        
    def calc_round_damage(self):
        total = 0
        for attack in self.attacks:
            total += attack.calc_total_damage()
        return total
    
    def display(self):
        result = f'Round {self.round_number}:'
        result = f'{result:<42}{self.calc_round_damage():>5.2f} Average Round Damage\n'
        
        if len(self.description) > 0:
            result += f'    {self.description}\n'

        for attack in self.attacks:
            result += f'{attack.display()}\n'
        return result
    
    def duplicate_round(self, new_round_number):
        return Round(new_round_number, self.attacks)
    
    def get_round_number(self):
        """
        This is needed to validate that a list[Round] is continuous and ordered.
        """
        return self.round_number
    
def validate_round_number(round_number: int):
    if round_number < 1:
        return 1
    if round_number > 50:
        return 50
    return round_number