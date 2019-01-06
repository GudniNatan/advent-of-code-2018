file = list()
with open("5-dec/input.txt") as file_pointer:
    file.extend(file_pointer)

polymer = file[0].strip()

char_list = [chr(i) for i in range(97, 123)]
char_combos = [c + c.upper() for c in char_list]
char_combos += [combo[::-1] for combo in char_combos]

last_polymer = None
while last_polymer != polymer:
    last_polymer = polymer
    for char_combo in char_combos:
        polymer = polymer.replace(char_combo, "")

print(len(polymer))
