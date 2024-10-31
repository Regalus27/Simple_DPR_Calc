from Attack import Attack
from characters.CharacterLoader import CharacterLoader
from DamageEvent import DamageEvent
from Utility import get_proficiency_mod, get_stat_mod, advantage_chance_recursive, great_weapon_master_attack_chance, validate_level, validate_percentage

class DougEldritchKnight(CharacterLoader):
    def __init__(self, level_max=20):
        self.level_max = validate_level(level_max)
        self.name = "Eldritch Knight"
        super().__init__(self.name, self.level_max)
    
    def set_up_attacks(self, level: int, round_number: int):
        return old_set_up_attacks(level, round_number)

"""
This only exists like this because I didn't want to add self. to every single command after this
"""
def old_set_up_attacks(level: int, round_number: int):
    level = validate_level(level)

    match level:
        case level if level <= 2:
            return [
                Attack("Greatsword", [
                    get_greatsword_damage_event(level)
                ])
            ]
        case level if level >= 3 and level <= 4:
            return [
                Attack("Booming Blade", [
                    get_greatsword_damage_event(level),
                    get_booming_blade_initial_damage_event(level),
                    get_booming_blade_triggered_damage_event(level)
                ])
            ]
        case 5:
            return [
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                ], number_of_attacks=2)
            ]
        case 6:
            return [
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                ], number_of_attacks=2),
                Attack("Great Weapon Mastery", [
                    get_great_weapon_mastery_damage_event(level, 2, graze=True),
                ])
            ]
        case level if level >= 7 and level <= 10:
            return [
                Attack("Booming Blade", [
                    get_greatsword_damage_event(level),
                    get_booming_blade_initial_damage_event(level),
                    get_booming_blade_triggered_damage_event(level)
                ]),
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                ]),
                Attack("Great Weapon Mastery", [
                    get_great_weapon_mastery_damage_event(level, 2, graze=True),
                ])
            ]
        case level if level >= 11 and level <= 12:
            return [
                Attack("Booming Blade", [
                    get_greatsword_damage_event(level),
                    get_booming_blade_initial_damage_event(level),
                    get_booming_blade_triggered_damage_event(level)
                ]),
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                ], number_of_attacks=2),
                Attack("Great Weapon Mastery", [
                    get_great_weapon_mastery_damage_event(level, 3, graze=True),
                ])
            ]
        # studied attacks
        case level if level >= 13 and level <= 19:
            previous_attacks = (round_number - 1) * 3
            return [
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                ], number_of_attacks=2, use_studied_attacks=True, studied_attacks_advantage_chance=advantage_chance_recursive(previous_attacks)),
                Attack("Booming Blade", [
                    get_greatsword_damage_event(level),
                    get_booming_blade_initial_damage_event(level),
                    get_booming_blade_triggered_damage_event(level)
                ], use_studied_attacks=True, studied_attacks_advantage_chance=advantage_chance_recursive(previous_attacks + 2)),
                Attack("Great Weapon Mastery", [
                    get_great_weapon_mastery_damage_event(level, 3, studied_attacks=True, graze=True),
                ])
            ]
        case 20:
            previous_attacks = (round_number - 1) * 4
            return [
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                ], number_of_attacks=3, use_studied_attacks=True, studied_attacks_advantage_chance=advantage_chance_recursive(previous_attacks)),
                Attack("Booming Blade", [
                    get_greatsword_damage_event(level),
                    get_booming_blade_initial_damage_event(level),
                    get_booming_blade_triggered_damage_event(level)
                ], use_studied_attacks=True, studied_attacks_advantage_chance=advantage_chance_recursive(previous_attacks + 3)),
                Attack("Great Weapon Mastery", [
                    get_great_weapon_mastery_damage_event(level, 4, studied_attacks=True, graze=True),
                ])
            ]
        case _:
            Attack("Unknown", [])

def get_booming_blade_initial_damage_event(level: int):
    level = validate_level(level)
    die_1 = 0
    if level >= 5 and level <= 10:
        die_1 = 1
    elif level >= 11 and level <= 16:
        die_1 = 2
    elif level >= 17:
        die_1 = 3
    
    return DamageEvent(die_1, 8, 0, "Booming Blade (Initial)")

def get_booming_blade_triggered_damage_event(level: int):
    level = validate_level(level)
    die_1 = 1
    if level >= 5 and level <= 10:
        die_1 = 2
    elif level >= 11 and level <= 16:
        die_1 = 3
    elif level >= 17:
        die_1 = 4

    conditional_chance = .25
    if level >= 9:
        conditional_chance = .5
    
    return DamageEvent(die_1, 8, 0, "Booming Blade (Trigger)", can_crit=False, conditional_chance=conditional_chance)

def get_greatsword_damage_event(level: int, graze_active=True):
    level = validate_level(level)

    damage_on_miss = 0
    if not graze_active:
        damage_on_miss = 0
    elif graze_active and level >= 9:
        # halving because at level 9+ I figure around half the time I'll be using push/another weapon trait, not graze
        damage_on_miss = get_stat_mod(level) / 2
    else:
        damage_on_miss = get_stat_mod(level)

    return DamageEvent(2, 6, 1 + get_stat_mod(level) + (get_proficiency_mod(level) if level >= 6 else 0),
                        "+1 Greatsword", damage_on_miss=damage_on_miss)

def get_great_weapon_mastery_damage_event(level: int, number_of_attacks_this_round: int, miss_chance=0.4, crit_chance=0.05,
                                    studied_attacks=False, initial_advantage_chance=0, graze=False):
    level = validate_level(level)
    miss_chance = validate_percentage(miss_chance)
    crit_chance = validate_percentage(crit_chance)

    activation_chance = great_weapon_master_attack_chance(number_of_attacks_this_round, miss_chance, crit_chance, studied_attacks, initial_advantage_chance)
    damage_on_miss = 0
    if graze:
        damage_on_miss = get_stat_mod(level)
    
    return DamageEvent(2, 6, 1 + get_stat_mod(level), "+1 Greatsword (GWM BA)", damage_on_miss=damage_on_miss, conditional_chance=activation_chance)