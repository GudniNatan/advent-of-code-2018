def diff_str(box1, box2):
    diff_list = list(box1)
    if len(box1) != len(box2):
        return ""
    for i in range(len(box1) - 1, -1, -1):
        if box1[i] != box2[i]:
            diff_list.pop(i)
    return "".join(diff_list)


file = list()
with open("2-dec/input.txt") as file_pointer:
    file.extend(file_pointer)

last_line = ""
for line in sorted(file):
    diff = diff_str(line, last_line)
    if len(diff) == len(line) - 1:
        print(diff)
    last_line = line
