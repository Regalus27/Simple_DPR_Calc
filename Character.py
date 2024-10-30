from Combat import Combat
import matplotlib.pyplot as plt
from Utility import validate_level

class Character:
    def __init__(self, name: str, combats: list[Combat], max_level=20):
        self.name = name
        self.max_level = validate_level(max_level)
        self.combats = validate_combats(combats, self.max_level)

    def graph_damage_per_combat(self, verbose=False):
        plot_x = [] # level
        plot_y = [] # damage number
        for i in range(1, len(self.combats) + 1):
            plot_x.append(i) # Level
            plot_y.append(self.combats[i-1].calc_damage_per_round()) # DPR
            print(self.combats[i-1].display(verbose))
        plt.plot(plot_x, plot_y)
        plt.axis((1, self.max_level, 0, 100))
        plt.xlabel('Level')
        plt.ylabel('Average DPR')
        plt.suptitle(f'{self.name} DPR')
        plt.show()

def validate_combats(combats: list[Combat], max_level: int):
    # Yeah I'm gonna ball and not write a unit test because my brain is tired
    # Surely I won't regret that
    combat_list = []
    for i in range(1, max_level + 1):
        found_flag = False
        for combat in combats:
            if combat.get_level() == i:
                combat_list.append(combat)
                found_flag = True
                break
        if not found_flag:
            if i == 1:
                combat_list.append(Combat(i, []))
            else:
                combat_list.append(combat_list[i-2].duplicate_combat(i))
    return combat_list