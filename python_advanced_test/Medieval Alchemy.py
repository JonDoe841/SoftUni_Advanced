from collections import deque

substances = deque(map(int, input().split(", ")))
crystals = deque(map(int, input().split(", ")))
potions = {110: "Brew of Immortality", 100: "Essence of Resilience", 90: "Draught of Wisdom",
           80:"Potion of Agility", 70: "Elixir of Strength"}
cauldron = 0
potions_done = []
while True:
    if not potions or not substances or not crystals:
        if not potions:
            print("Success! The alchemist has forged all potions!")
        elif potions:
            print("The alchemist failed to complete his quest.")
        if potions_done:
            print(f"Crafted potions: {', '.join(potions_done)}")
        if substances:
            print(f"Substances: {', '.join(map(str, reversed(substances)))}")
        if crystals:
            print(f"Crystals: {', '.join(map(str, crystals))}")
        break
    cauldron = 0
    curr_sub = substances.pop()
    curr_crystal = crystals.popleft()
    cauldron += curr_sub +curr_crystal
    if cauldron in potions:
        potions_done.append(potions.pop(cauldron))
    else:
        possible_potions = [p for p in potions if p < cauldron]
        if possible_potions:
            best_potion = max(possible_potions)
            potions_done.append(potions.pop(best_potion))
            if curr_crystal > 20:
                crystals.append(curr_crystal - 20)
        else:
            if curr_crystal > 5:
                crystals.append(curr_crystal - 5)