from Round import Round
from Utility import validate_level

class Combat:
    """
    Combat tracks all rounds in a theoretical combat scenario, then provides
    an average damage over those rounds. Useful for distinguishing between burst
    and sustained damage.

    The final round in a combat is assumed to be a sustained DPS state.
    """
    def __init__(self, level: int, rounds: list[Round], tactics_description='', combat_length=4):
        if combat_length < 1:
            self.combat_length = 1
        elif combat_length > 50:
            self.combat_length = 50
        else:
            self.combat_length = combat_length

        self.description = tactics_description
        self.level = validate_level(level)
        self.rounds = validate_rounds(rounds, combat_length)

    def calc_damage_per_round(self):
        """
        Returns the average DPR over this combat
        
        By default, assumes combat lasts 4 rounds
        If not enough rounds are provided to fill the combat_length,
        the final round will have its damage value repeated (sustained DPR)

        Max combat_length is 50.
        """
        total = 0
        for round in self.rounds:
            total += round.calc_round_damage()
        return total / self.combat_length
    
    def display(self, verbose=False):
        """
        Level X:    X Average DPR\n
            Description\n
        for round in rounds display
        """
        result = f'Level {self.level}:'
        result = f'{result:<42}{self.calc_damage_per_round():>5.2f} Average DPR\n'

        if len(self.description) > 0:
            result += f'    {self.description}\n\n'

        if verbose:
            for round in self.rounds:
                result += f'{round.display()}\n'

        return result
    
    def duplicate_combat(self, new_level):
        return Combat(new_level, self.rounds)
    
    def get_level(self):
        return self.level

def validate_rounds(rounds: list[Round], combat_length: int):
        """
        This is less validation and more forceful formatting

        oh wait I'm silly, this is way easier
        Iterate over rounds
            search for round i
            if find add to round_list and break
            else either duplicate previous round or create empty round
            continue until > combat length
        
        round_list should now be continuous and no duplicates from 1 - combat_length
        """
        round_list = []
        for i in range(1, combat_length + 1):
            round_found_flag = False
            for round in rounds:
                if round.get_round_number() == i:
                    round_list.append(round)
                    round_found_flag = True
                    break
            if not round_found_flag:
                """
                If no round was found on round 1
                    i == 1
                    len(round_list) == 0 (i-1)
                    Add empty Round
                """
                if i == 1:
                    round_list.append(Round(i, []))
                else:
                    """
                    If not round 1, duplicate previous round
                    i == 2
                    len(round_list) == 1
                    need round_list[0] (i-2)
                    """
                    round_list.append(round_list[i-2].duplicate_round(i))
        return round_list