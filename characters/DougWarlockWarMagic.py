from Attack import Attack
from Character import Character
from Combat import Combat
from DamageEvent import DamageEvent
from Round import Round
from characters.CharacterLoader import CharacterLoader
from Utility import get_proficiency_mod, get_stat_mod, validate_level

class DougWarlockWarMagic(CharacterLoader):
    def get_character(max_level=14):
        max_level = validate_level(max_level)
        return Character("Doug Dugorok (Warlock, War Magic)", set_up_combats(), max_level)

"""
The below works, but is not guaranteed to be a good framework to copy-paste into future characters
"""
def set_up_combats():
    result = []

    result.append(Combat(1, set_up_rounds(1), "Orc Rush, then Hex. Booming Blade DPR."))
    result.append(Combat(2, set_up_rounds(2), "Orc Rush, then Hex. Booming Blade DPR w/ Repelling Blast."))
    result.append(Combat(3, set_up_rounds(3), "Orc Rush, Hex, Hexblade's Curse. Booming Blade."))
    result.append(Combat(4, set_up_rounds(4), "Orc Rush, Hex, Hexblade's Curse. Booming Blade."))
    result.append(Combat(5, set_up_rounds(5), "Greatsword x2"))
    result.append(Combat(6, set_up_rounds(6), "Delaying War Magic to Level 7 for balance purposes"))
    result.append(Combat(7, set_up_rounds(7), "War Magic, Agonizing Blast (from level 5)"))
    result.append(Combat(8, set_up_rounds(8), "War Magic"))
    result.append(Combat(9, set_up_rounds(9), "Lifedrinker"))
    result.append(Combat(10, set_up_rounds(10), "War Magic"))
    result.append(Combat(11, set_up_rounds(11), "War Magic"))
    result.append(Combat(12, set_up_rounds(12), "Devouring Blade and Great Weapon Master"))
    result.append(Combat(13, set_up_rounds(13), "Devouring Blade and Great Weapon Master"))
    result.append(Combat(14, set_up_rounds(14), "Devouring Blade and Great Weapon Master"))

    return result

def set_up_rounds(level: int):
    result = []
    match level:
        case 1:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade"))
        case 2:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade"))
        case 3:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade"))
        case 4:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade"))
        case 5:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Greatsword x2"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Greatsword x2"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Greatsword x2"))
        case 6:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Greatsword x2"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Greatsword x2"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Greatsword x2"))
        case 7:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade, Greatsword"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade, Greatsword"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade, Greatsword"))
        case 8:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade, Greatsword"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade, Greatsword"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade, Greatsword"))
        case 9:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade, Greatsword"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade, Greatsword"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade, Greatsword"))
        case 10:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade, Greatsword"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade, Greatsword"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade, Greatsword"))
        case 11:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade, Greatsword"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade, Greatsword"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade, Greatsword"))
        case 12:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade, Greatsword x2"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade, Greatsword x2"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade, Greatsword x2"))
        case 13:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade, Greatsword x2"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade, Greatsword x2"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade, Greatsword x2"))
        case 14:
            result.append(Round(1, set_up_attacks(level, 1), "Orc Rush, Booming Blade, Greatsword x2"))
            result.append(Round(2, set_up_attacks(level, 2), "Hex, Booming Blade, Greatsword x2"))
            result.append(Round(3, set_up_attacks(level, 3), "Hexblade's Curse, Booming Blade, Greatsword x2"))
        case _:
            pass
    return result

def set_up_attacks(level: int, round_number: int):
    result = []
    match (level, round_number):
        case (1, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number)))
        case (1, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number)))

        case (2, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number)))
        case (2, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number)))

        case (3, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number)))
        case (3, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number)))
        case (3, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), crit_chance=.1))

        case (4, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number)))
        case (4, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number)))
        case (4, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), crit_chance=.1))
        
        case (5, 1):
            result.append(Attack("Greatsword", set_up_damage_events(level, 1, round_number), number_of_attacks=2))
        case (5, 2):
            result.append(Attack("Greatsword", set_up_damage_events(level, 1, round_number), number_of_attacks=2))
        case (5, 3):
            result.append(Attack("Greatsword", set_up_damage_events(level, 1, round_number), number_of_attacks=2, crit_chance=0.1))

        case (6, 1):
            result.append(Attack("Greatsword", set_up_damage_events(level, 1, round_number), number_of_attacks=2))
        case (6, 2):
            result.append(Attack("Greatsword", set_up_damage_events(level, 1, round_number), number_of_attacks=2))
        case (6, 3):
            result.append(Attack("Greatsword", set_up_damage_events(level, 1, round_number), number_of_attacks=2, crit_chance=0.1))

        case (7, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (7, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (7, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1, crit_chance=0.1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1, crit_chance=0.1))

        case (8, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (8, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (8, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1, crit_chance=0.1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1, crit_chance=0.1))

        case (9, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (9, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (9, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1, crit_chance=0.1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1, crit_chance=0.1))

        case (10, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (10, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (10, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1, crit_chance=0.1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1, crit_chance=0.1))

        case (11, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (11, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1))
        case (11, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1, crit_chance=0.1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=1, crit_chance=0.1))

        case (12, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=2))
        case (12, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=2))
        case (12, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1, crit_chance=0.1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=2, crit_chance=0.1))

        case (13, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=2))
        case (13, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=2))
        case (13, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1, crit_chance=0.1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=2, crit_chance=0.1))

        case (14, 1):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=2))
        case (14, 2):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=2))
        case (14, 3):
            result.append(Attack("Booming Blade", set_up_damage_events(level, 1, round_number), number_of_attacks=1, crit_chance=0.1))
            result.append(Attack("Greatsword", set_up_damage_events(level, 2, round_number), number_of_attacks=2, crit_chance=0.1))

        case _:
            pass
    return result

def set_up_damage_events(level: int, attack_number: int, round_number: int):
    """
    Future upgrades:
        Add usesStatMod to DamageEvent to trigger what to add to flat damage
        Add usesProfMod (Hexblade's Curse) to DamageEvent to trigger what to add to flat damage
    """
    result = []
    # Oh this is going to be awful to set up
    match (level, attack_number, round_number):
        case (1, 1, 1):
            # Booming Blade
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.1))
        case (1, 1, 2):
            # Booming Blade and Hex
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.1))
        
        case (2, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (2, 1, 2):
            # Booming Blade and Hex
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))

        case (3, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (3, 1, 2):
            # Booming Blade and Hex
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (3, 1, 3):
            # Booming Blade and Hex and Hexblade's Curse
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))

        case (4, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (4, 1, 2):
            # Booming Blade and Hex
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (4, 1, 3):
            # Booming Blade and Hex and Hexblade's Curse
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))

        case (5, 1, 1):
            # Double greatsword swing, Orc Rush
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
        case (5, 1, 2):
            # Double greatsword swing, Hex
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
        case (5, 1, 3):
            # Double greatsword swing, Hex, Hexblade's Curse
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))

        case (6, 1, 1):
            # Double greatsword swing, Orc Rush
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
        case (6, 1, 2):
            # Double greatsword swing, Hex
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
        case (6, 1, 3):
            # Double greatsword swing, Hex, Hexblade's Curse
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))

        # We are delaying War Magic to Level 7 for balance purposes
        case (7, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (7, 2, 1):
            # Orc Rush, Greatsword only
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
        case (7, 1, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (7, 2, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
        case (7, 1, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (7, 2, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))

        case (8, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (8, 2, 1):
            # Orc Rush, Greatsword only
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
        case (8, 1, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (8, 2, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
        case (8, 1, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (8, 2, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))

        case (9, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (9, 2, 1):
            # Orc Rush, Greatsword only
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (9, 1, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (9, 2, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (9, 1, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (9, 2, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))

        case (10, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (10, 2, 1):
            # Orc Rush, Greatsword only
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (10, 1, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (10, 2, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (10, 1, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (10, 2, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))

        case (11, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (11, 2, 1):
            # Orc Rush, Greatsword only
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (11, 1, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (11, 2, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (11, 1, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (11, 2, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))

        case (12, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (12, 2, 1):
            # Orc Rush, Greatsword only
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (12, 1, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (12, 2, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (12, 1, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (12, 2, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))

        case (13, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (13, 2, 1):
            # Orc Rush, Greatsword only
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (13, 1, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (13, 2, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (13, 1, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (13, 2, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))

        case (14, 1, 1):
            # Orc Rush, Booming Blade (Repelling)
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (14, 2, 1):
            # Orc Rush, Greatsword only
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (14, 1, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (14, 2, 2):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))
        case (14, 1, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(2, 8, get_stat_mod(level), "Booming Blade"))
            result.append(DamageEvent(3, 8, get_stat_mod(level), "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.5))
        case (14, 2, 3):
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(level) + get_proficiency_mod(level), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse"))
            result.append(DamageEvent(1, 6, 0, "Lifedrinker"))

        case _:
            pass
    return result