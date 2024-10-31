from Character import Character
from characters.DougWarlockWarMagicUpdated import DougWarlockWarMagicUpdated
from characters.DougWarlockNoWarMagic import DougWarlockNoWarMagic
from characters.DougEldritchKnight import DougEldritchKnight
from itertools import cycle
import matplotlib.pyplot as plt
from Utility import great_weapon_master_attack_chance
from characters.DougEldritchKnight import get_great_weapon_mastery_damage_event

def main():
    characters = []
    
    doug_ek = DougEldritchKnight(20).get_character()
    characters.append(doug_ek)
    # doug_ek.graph_damage_per_combat(True)

    graph_damage_per_character(characters)

def graph_damage_per_character(characters: list[Character]):
    # random colors, ty user3240588 from stackoverflow
    cycle_colors = cycle('gbrcmk')

    # There's probably a super easy way to generate this, but it was faster to type it
    plot_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # Levels
    for character in characters:
        plot_y = []
        for i in range(1, len(character.combats) + 1):
            plot_y.append(character.combats[i-1].calc_damage_per_round()) # DPR
        plt.plot(plot_x, plot_y, color=next(cycle_colors), label=character.name)
    
    plt.xlabel("Level")
    plt.ylabel("Average Damage Per Round")
    plt.suptitle("Character DPR Comparison")
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()