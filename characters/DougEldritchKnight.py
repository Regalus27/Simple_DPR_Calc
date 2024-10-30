from Attack import Attack
from Character import Character
from Combat import Combat
from DamageEvent import DamageEvent
from Round import Round
from Utility import get_proficiency_mod, get_stat_mod, validate_level

class DougEldritchKnight():
    def get_character(max_level: int):
        max_level = validate_level(max_level)
        return Character("Doug Eldritch Knight", set_up_combats(max_level), max_level)
    
def set_up_combats(max_level: int):
    max_level = validate_level(max_level)
    result = []

    for i in range(1, max_level + 1):
        result.append(Combat(i, set_up_rounds(i), set_up_combat_description(i)))
    
    return result

def set_up_combat_description(level: int):
    level = validate_level(level)

    match level:
        case _:
            return ""
        
def set_up_rounds(level: int, max_rounds=4):
    level = validate_level(level)
    
    if max_rounds < 1:
        max_rounds = 1
    elif max_rounds > 50:
        max_rounds = 50

    rounds = []

    for round in range(1, max_rounds + 1):
        rounds.append(Round(round, set_up_attacks(level, round)))

    return rounds

def set_up_attacks(level: int, round_number: int):
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
                    get_hex_damage_event(round_number),
                    get_booming_blade_initial_damage_event(level),
                    get_booming_blade_triggered_damage_event(level)
                ])
            ]
        case level if level >= 5 and level <= 6:
            return [
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                    get_hex_damage_event(round_number)
                ], number_of_attacks=2)
            ]
        case level if level >= 7 and level <= 10:
            return [
                Attack("Booming Blade", [
                    get_greatsword_damage_event(level),
                    get_hex_damage_event(round_number),
                    get_booming_blade_initial_damage_event(level),
                    get_booming_blade_triggered_damage_event(level)
                ]),
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                    get_hex_damage_event(round_number)
                ])
            ]
        case level if level >= 11 and level <= 19:
            return [
                Attack("Booming Blade", [
                    get_greatsword_damage_event(level),
                    get_hex_damage_event(round_number),
                    get_booming_blade_initial_damage_event(level),
                    get_booming_blade_triggered_damage_event(level)
                ]),
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                    get_hex_damage_event(round_number)
                ], number_of_attacks=2)
            ]
        case 20:
            return [
                Attack("Booming Blade", [
                    get_greatsword_damage_event(level),
                    get_hex_damage_event(round_number),
                    get_booming_blade_initial_damage_event(level),
                    get_booming_blade_triggered_damage_event(level)
                ]),
                Attack("Greatsword", [
                    get_greatsword_damage_event(level),
                    get_hex_damage_event(round_number)
                ], number_of_attacks=3)
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

def get_hex_damage_event(round_number: int):
    if round_number > 1:
        return DamageEvent(1, 6, 0, "Hex")
    return DamageEvent(0, 0, 0, "Hex (Uncast)")
"""
Could I define specific common damage sources and just use those?
    Booming Blade
    +1 Greatsword
Or rather, I could set up specific common attacks and set up automatic scaling?
    Booming Blade
        Greatsword Hit
        Booming Blade (Initial)
        Booming Blade (Triggered)
What about Hex, Hexblade's Curse, other temporary effects?
    Attack Modifier?
    Just another Damage Event added to the list?
Goal here would be to be able to say at the combat level:
    Level 5:
        Greatsword Attack x2
        Add Hex Damage starting round 2
And have it just work.
    Level 1:
        Greatsword Attack x1
    Level 2: 
        Greatsword Attack x1
    Level 3:
        Booming Blade x1 (mid chance, tactical mind)
        Hex & Booming Blade beginning Round 2
    Level 4:
        Booming Blade x1
        Hex & Booming Blade beginning Round 2
    Level 5:
        Greatsword x2
        Hex Round 2
    Level 6:
        Greatsword x2
        Hex Round 2
    Level 7:
        Greatsword x1
        Booming Blade x1
        Hex Round 2
    Level 8:
        Greatsword x1
        Booming Blade x1
        Hex Round 2
    Level 9:
        Greatsword x1
        Booming Blade x1 (Push weapons, 50%, lose Graze on first attack?)
        Hex Round 2
    Level 10:
        Greatsword x1
        Booming Blade x1
        Hex Round 2
    Level 11:
        Greatsword x2
        Booming Blade x1
        Hex Round 2
    Level 12:
        Greatsword x2
        Booming Blade x1
        Hex Round 2
    Level 13:
        STUDIED ATTACKS OH NO
            chance to miss w/ advantage: .105
            chance to hit w/ advantage:  .7975
            chance to crit w/ advantage: .0975
            sums to:                    1.0
            but how to know when to apply this bonus?
                assumes always attacking the same target
                
        Greatsword x2
        Booming Blade x1
        Hex Round 2
    Level 14:
        Greatsword x2
        Booming Blade x1
        Hex Round 2
"""