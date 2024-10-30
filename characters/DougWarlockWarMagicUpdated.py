from Attack import Attack
from Character import Character
from Combat import Combat
from DamageEvent import DamageEvent
from Round import Round
from characters.CharacterLoader import CharacterLoader
from Utility import get_proficiency_mod, get_stat_mod, validate_level

class DougWarlockWarMagicUpdated(CharacterLoader):
    def __init__(self, level_max=20):
        self.level_max = validate_level(level_max)
        self.name = "OP Warlock w/ War Magic"
        super().__init__(self.name, self.level_max)

    def set_up_attacks(self, level: int, round_number: int):
        level = validate_level(level)

        match level:
            case level if level <=4:
                return [
                    Attack("Booming Blade", [
                        self.get_greatsword_damage_event(level),
                        self.get_hex_damage_event(round_number),
                        self.get_hexblade_curse_damage_event(level, round_number),
                        self.get_booming_blade_initial_damage_event(level),
                        self.get_booming_blade_triggered_damage_event(level)
                    ])
                ]
            case level if level == 5 or level == 6:
                return [
                    Attack("Greatsword", [
                        self.get_greatsword_damage_event(level),
                        self.get_hex_damage_event(round_number),
                        self.get_hexblade_curse_damage_event(level, round_number)
                    ], number_of_attacks=2)
                ]
            case level if level >= 7 and level <= 11:
                return [
                    Attack("Booming Blade", [
                        self.get_greatsword_damage_event(level),
                        self.get_hex_damage_event(round_number),
                        self.get_hexblade_curse_damage_event(level, round_number),
                        self.get_lifedrinker_damage_event(level),
                        self.get_booming_blade_initial_damage_event(level),
                        self.get_booming_blade_triggered_damage_event(level)
                    ]),
                    Attack("Greatsword", [
                        self.get_greatsword_damage_event(level),
                        self.get_hex_damage_event(round_number),
                        self.get_hexblade_curse_damage_event(level, round_number)
                    ], number_of_attacks=1)
                ]
            case level if level >= 12 and level <= 20:
                return [
                    Attack("Booming Blade", [
                        self.get_greatsword_damage_event(level),
                        self.get_hex_damage_event(round_number),
                        self.get_hexblade_curse_damage_event(level, round_number),
                        self.get_lifedrinker_damage_event(level),
                        self.get_booming_blade_initial_damage_event(level),
                        self.get_booming_blade_triggered_damage_event(level)
                    ]),
                    Attack("Greatsword", [
                        self.get_greatsword_damage_event(level),
                        self.get_hex_damage_event(round_number),
                        self.get_hexblade_curse_damage_event(level, round_number)
                    ], number_of_attacks=2)
                ]
            case _:
                return []
            

    """
    Needed Attacks:
        Booming Blade (increase modifier to .5 level 2+)
        +1 Greatsword
        Hex
    
    Need to add Hexblade Curse to rounds 3+
        Modifier to attacks, just need to have a global check where
            crit_chance = 0.5
            if level >= 3 AND round_number >= 3
                crit_chance = 0.1
        and modify each attack to include that
        additionally, add a damage source that cannot crit called hexblade_curse
            on round 1 & 2, 0 damage (uncast)
            on round 3, add proficiency mod
    """

    def get_booming_blade_initial_damage_event(self, level: int):
        # Add check for level to account for Agonizing Blast
        level = validate_level(level)
        die_1 = 0
        if level >= 5 and level <= 10:
            die_1 = 1
        elif level >= 11 and level <= 16:
            die_1 = 2
        elif level >= 17:
            die_1 = 3

        agonizing_blast_damage = 0
        if level >= 2:
            agonizing_blast_damage = get_proficiency_mod(level)
        
        return DamageEvent(die_1, 8, agonizing_blast_damage, "Booming Blade (Initial)")
    
    def get_booming_blade_triggered_damage_event(self, level: int):
        level = validate_level(level)
        die_1 = 1
        if level >= 5 and level <= 10:
            die_1 = 2
        elif level >= 11 and level <= 16:
            die_1 = 3
        elif level >= 17:
            die_1 = 4

        agonizing_blast_damage = 0
        conditional_chance = .1
        if level >= 2:
            agonizing_blast_damage = get_proficiency_mod(level)
            conditional_chance = .5

        return DamageEvent(die_1, 8, agonizing_blast_damage, "Booming Blade (Trigger)",
                           can_crit=False, conditional_chance=conditional_chance)

    def get_greatsword_damage_event(self, level: int):
        level = validate_level(level)

        flat_damage = 1 + get_stat_mod(level)
        if level >= 12:
            # Great Weapon Mastery
            flat_damage = 1 + get_stat_mod(level) + get_proficiency_mod(level)

        return DamageEvent(2, 6, flat_damage, "+1 Greatsword")
    
    def get_hex_damage_event(self, round_number: int):
        if round_number >= 2:
            return DamageEvent(1, 6, 0, "Hex")
        return DamageEvent(0, 0, 0, "Hex (Uncast)")
    
    def get_hexblade_curse_damage_event(self, level: int, round_number: int):
        if round_number >= 3 and level >= 3:
            return DamageEvent(0, 0, get_proficiency_mod(level), "Hexblade's Curse")
        return DamageEvent(0, 0, 0, "Hexblade's Curse (Uncast)")
    
    def get_lifedrinker_damage_event(self, level: int):
        if level >= 9:
            return DamageEvent(1, 8, 0, "Lifedrinker Invocation")
        return DamageEvent(0, 0, 0, "Lifedrinker Invocation (Too low Level)")