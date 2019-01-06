def exact_count(line: str, count) -> bool:
    for char in line:
        if line.count(char) == count:
            return True
    return False

doubles = 0
triples = 0

file = list()
with open("2-dec/input.txt") as file_pointer:
    file.extend(file_pointer)

for line in file:
    if exact_count(line, 2):
        doubles += 1
    if exact_count(line, 3):
        triples += 1

print(doubles * triples)
