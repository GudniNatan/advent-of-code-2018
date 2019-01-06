seen = set()
total = 0
first_repeat = None

file = list()
with open("1-dec/input.txt") as file_pointer:
    file.extend(file_pointer)

while first_repeat is None:
    for line in file:
        if line[0] == "+":
            total += int(line[1:])
        else:
            total -= int(line[1:])
        if total in seen:
            first_repeat = total
            break
        seen.add(total)

print(total)
