from Character import Character
from characters.DougWarlockWarMagicUpdated import DougWarlockWarMagicUpdated
from characters.DougEldritchKnight import DougEldritchKnight
from itertools import cycle
import matplotlib.pyplot as plt

def main():
    doug_warlock = DougWarlockWarMagicUpdated(20).get_character()
    # doug_warlock.graph_damage_per_combat()

    doug_ek = DougEldritchKnight(20).get_character()
    # doug_ek.graph_damage_per_combat(20)

    characters = []
    characters.append(doug_warlock)
    characters.append(doug_ek)
    graph_damage_per_character(characters)

def graph_damage_per_character(characters: list[Character]):
    # random colors, ty user3240588 from stackoverflow
    cycle_colors = cycle('bgrcmk')

    # There's probably a super easy way to generate this, but it was faster to type it
    plot_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # Levels
    # plot_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for character in characters:
        plot_y = []
        for i in range(1, len(character.combats) + 1):
            plot_y.append(character.combats[i-1].calc_damage_per_round()) # DPR
        plt.plot(plot_x, plot_y, color=next(cycle_colors), label=character.name)
    
    plt.xlabel("Label")
    plt.ylabel("Average DPR")
    plt.suptitle("Various Doug DPRs")
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()