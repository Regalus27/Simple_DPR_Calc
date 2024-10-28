from DamageEvent import DamageEvent
from Attack import Attack

def main():
    # ALL OF THIS IS AWFUL AND TEMPORARY PLEASE DON'T PERCEIVE IT ;-;

    booming_blade_damage_events = []
    booming_blade_damage_events.append(DamageEvent(2, 6, 4, name="+1 Greatsword"))
    booming_blade_damage_events.append(DamageEvent(0, 8, 0, name="Booming Blade (Initial)"))
    booming_blade_damage_events.append(DamageEvent(1, 8, 0, name="Booming Blade (Detonation)", can_crit=False, conditional_chance=.25))
    
    booming_blade_attack = Attack("Level 1 Booming Blade", booming_blade_damage_events, 1)
    print(booming_blade_attack.display())

    booming_blade_damage_events = []
    booming_blade_damage_events.append(DamageEvent(2, 6, 4, name="+1 Greatsword"))
    booming_blade_damage_events.append(DamageEvent(0, 8, 0, name="Booming Blade (Initial)"))
    booming_blade_damage_events.append(DamageEvent(1, 8, 0, name="Booming Blade (Detonation)", can_crit=False, conditional_chance=.5))
    
    booming_blade_attack = Attack("Level 2 Booming Blade", booming_blade_damage_events, 1)
    print(booming_blade_attack.display())

    booming_blade_damage_events = []
    booming_blade_damage_events.append(DamageEvent(2, 6, 4, name="+1 Greatsword"))
    booming_blade_damage_events.append(DamageEvent(0, 8, 0, name="Booming Blade (Initial)"))
    booming_blade_damage_events.append(DamageEvent(1, 8, 0, name="Booming Blade (Detonation)", can_crit=False, conditional_chance=.5))
    booming_blade_damage_events.append(DamageEvent(0, 0, 2, name="Hexblade's Curse"))
    
    booming_blade_attack = Attack("Level 3 Booming Blade", booming_blade_damage_events, 1, crit_chance=0.1)
    print(booming_blade_attack.display())

    booming_blade_damage_events = []
    booming_blade_damage_events.append(DamageEvent(2, 6, 5, name="+1 Greatsword"))
    booming_blade_damage_events.append(DamageEvent(0, 8, 0, name="Booming Blade (Initial)"))
    booming_blade_damage_events.append(DamageEvent(1, 8, 0, name="Booming Blade (Detonation)", can_crit=False, conditional_chance=.5))
    booming_blade_damage_events.append(DamageEvent(0, 0, 2, name="Hexblade's Curse"))
    
    booming_blade_attack = Attack("Level 4 Booming Blade", booming_blade_damage_events, 1, crit_chance=0.1)
    print(booming_blade_attack.display())

    booming_blade_damage_events = []
    booming_blade_damage_events.append(DamageEvent(2, 6, 5, name="+1 Greatsword"))
    booming_blade_damage_events.append(DamageEvent(0, 0, 3, name="Hexblade's Curse"))
    
    booming_blade_attack = Attack("Level 5 2x Basic Attack", booming_blade_damage_events, 2, crit_chance=0.1)
    print(booming_blade_attack.display())

def populate_attacks():
    pass

if __name__ == "__main__":
    main()