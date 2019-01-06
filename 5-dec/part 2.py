from math import inf

file = list()
with open("5-dec/input.txt") as file_pointer:
    file.extend(file_pointer)

polymer = file[0].strip()

char_list = [chr(i) for i in range(97, 123)]
char_combos = [c + c.upper() for c in char_list]
char_combos += [combo[::-1] for combo in char_combos]

polymer_min = inf
for char in char_list:
    free_polymer = polymer.replace(char, "").replace(char.upper(), "")
    last_polymer = None
    while last_polymer != free_polymer:
        last_polymer = free_polymer
        for char_combo in char_combos:
            free_polymer = free_polymer.replace(char_combo, "")
    polymer_min = min(polymer_min, len(free_polymer))

print(polymer_min)
