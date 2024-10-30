from abc import ABC, abstractmethod
from Character import Character
from Combat import Combat
from Round import Round
from Utility import validate_level

class CharacterLoader(ABC):
    def __init__(self, name: str, level_max=20):
        self.level_max = validate_level(level_max)
        self.name = name

    def get_character(self):
        return Character(self.name, self.set_up_combats(), self.level_max)
    
    def set_up_combats(self):
        result = []
        for i in range(1, self.level_max + 1):
            result.append(Combat(i, self.set_up_rounds(i), self.set_up_combat_description(i)))
        return result

    # This should be overridden if you want to have descriptions.
    def set_up_combat_description(self, level:int):
        return ""

    def set_up_rounds(self, level: int,  max_rounds=4):
        level = validate_level(level)

        if max_rounds < 1:
            max_rounds = 1
        elif max_rounds > 50:
            max_rounds = 50

        rounds = []

        for round in range(1, max_rounds + 1):
            rounds.append(Round(round, self.set_up_attacks(level, round)))

        return rounds
    
    @abstractmethod
    def set_up_attacks(self, level: int, round_number: int):
        pass
