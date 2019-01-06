total = 0
file = list()
with open("1-dec/input.txt") as file_pointer:
    file.extend(file_pointer)

for line in file:
    if line[0] == "+":
        total += int(line[1:])
    else:
        total -= int(line[1:])

print(total)
