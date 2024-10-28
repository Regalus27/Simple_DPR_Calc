from Attack import Attack
from DamageEvent import DamageEvent
from Round import Round

def main():
    rounds = []

    # Round One
    temp_damage_events = []
    temp_damage_events.append(DamageEvent(2, 6, 4, name="+1 Greatsword"))
    temp_damage_events.append(DamageEvent(0, 8, 0, name="Booming Blade (Initial)"))
    temp_damage_events.append(DamageEvent(1, 8, 0, name="Booming Blade (Trigger)", can_crit=False, conditional_chance=.25))
    booming_blade_attack = Attack("Booming Blade", temp_damage_events, 1)
    rounds.append(Round(1, [booming_blade_attack], "I cast Booming Blade."))

    for round in rounds:
        print(round.display())

    """# Round Two
    temp_damage_events = []
    temp_damage_events.append(DamageEvent(2, 6, 4, name="+1 Greatsword"))
    temp_damage_events.append(DamageEvent(0, 8, 0, name="Booming Blade (Initial)"))
    temp_damage_events.append(DamageEvent(1, 8, 0, name="Booming Blade (Detonation)", can_crit=False, conditional_chance=.5))
    
    booming_blade_attack = Attack("Booming Blade", temp_damage_events, 1)
    print(booming_blade_attack.display())

    temp_damage_events = []
    temp_damage_events.append(DamageEvent(2, 6, 4, name="+1 Greatsword"))
    temp_damage_events.append(DamageEvent(0, 8, 0, name="Booming Blade (Initial)"))
    temp_damage_events.append(DamageEvent(1, 8, 0, name="Booming Blade (Detonation)", can_crit=False, conditional_chance=.5))
    temp_damage_events.append(DamageEvent(0, 0, 2, name="Hexblade's Curse"))
    
    booming_blade_attack = Attack("Booming Blade", temp_damage_events, 1, crit_chance=0.1)
    print(booming_blade_attack.display())

    temp_damage_events = []
    temp_damage_events.append(DamageEvent(2, 6, 5, name="+1 Greatsword"))
    temp_damage_events.append(DamageEvent(0, 8, 0, name="Booming Blade (Initial)"))
    temp_damage_events.append(DamageEvent(1, 8, 0, name="Booming Blade (Detonation)", can_crit=False, conditional_chance=.5))
    temp_damage_events.append(DamageEvent(0, 0, 2, name="Hexblade's Curse"))
    
    booming_blade_attack = Attack("Booming Blade", temp_damage_events, 1, crit_chance=0.1)
    print(booming_blade_attack.display())

    temp_damage_events = []
    temp_damage_events.append(DamageEvent(2, 6, 5, name="+1 Greatsword"))
    temp_damage_events.append(DamageEvent(0, 0, 3, name="Hexblade's Curse"))
    
    booming_blade_attack = Attack("2x Basic Attack", temp_damage_events, 2, crit_chance=0.1)
    print(booming_blade_attack.display())"""

if __name__ == "__main__":
    main()