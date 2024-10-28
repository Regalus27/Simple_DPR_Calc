from Attack import Attack
from Combat import Combat
from DamageEvent import DamageEvent
from Round import Round

def main():
    rounds = []
    # Level 1, Round 1, Attack 1
    # Booming Blade
    rounds.append(Round(1, [Attack("Booming Blade", set_up_damage_events(1, 1, 1))], "Orc Rush, then Booming Blade"))

    # Level 1, Round 1, Attack 2
    rounds.append(Round(2, [Attack("Booming Blade", set_up_damage_events(1, 1, 2))], "Hex, then Booming Blade."))

    level_one_combat = Combat(1, rounds, "Orc Rush and Booming Blade as an opener. Cast Hex Round 2.", )

    print(level_one_combat.display(verbose=False))
    print("Verbose Mode:")
    print(level_one_combat.display(verbose=True))

# Level 5 test
def get_proficiency_mod(level: int):
    mod = 0
    match level:
        case level if level >= 1 and level <= 4:
            mod = 2
        case level if level >= 5 and level <= 8:
            mod = 3
        case level if level >= 9 and level <= 12:
            mod = 4
        case level if level >= 13 and level <= 16:
            mod = 5
        case level if level >= 17 and level <= 20:
            mod = 6
        case _:
            mod = 0
    return mod

def get_stat_mod(level: int):
    """
    Assumes +3 level 1, +4 level 4, +5 level 8+
    """
    mod = 0
    match level:
        case level if level >= 1 and level <= 3:
            mod = 3
        case level if level >= 4 and level <= 7:
            mod = 4
        case level if level >= 8 and level <= 20:
            mod = 5
        case _:
            mod = 0
    return mod

def set_up_combats():
    pass

def set_up_rounds():
    pass

def set_up_attacks():
    pass

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
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(1), "+1 Greatsword"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.25))
        case (1, 1, 2):
            # Booming Blade and Hex
            result.append(DamageEvent(2, 6, 1 + get_stat_mod(1), "+1 Greatsword"))
            result.append(DamageEvent(1, 6, 0, "Hex"))
            result.append(DamageEvent(0, 8, 0, "Booming Blade"))
            result.append(DamageEvent(1, 8, 0, "Booming Blade (Triggered)", can_crit=False, conditional_chance=0.25))    
        case _:
            pass
    return result

if __name__ == "__main__":
    main()