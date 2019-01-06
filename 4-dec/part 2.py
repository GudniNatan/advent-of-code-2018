from datetime import datetime

file = list()
with open("4-dec/input.txt") as file_pointer:
    file.extend(file_pointer)

ordered_items = list()
guard_patterns = dict()

for line in file:
    timestamp = line[:18]
    message = line[19:]
    time = datetime.strptime(timestamp, "[%Y-%m-%d %H:%M]")
    ordered_items.append((time, message))

ordered_items.sort()
guard = None
for i, line in enumerate(ordered_items):
    message = line[1]
    if message[0] == "G":
        guard = int(message.split()[1][1:])
        continue
    try:
        guard_patterns[guard].append(line)
    except KeyError:
        guard_patterns[guard] = [line]

sleep = dict()
for guard in guard_patterns.keys():
    sleep[guard] = [0 for _ in range(60)]

for guard, patterns in guard_patterns.items():
    last_sleep = None
    for pattern in patterns:
        if pattern[1][0] == "f":
            last_sleep = pattern[0]
        else:
            for i in range(last_sleep.minute, pattern[0].minute):
                sleep[guard][i] += 1

max_guard = None
max_mins = 0
for guard, minutes in sleep.items():
    if max(minutes) > max_mins:
        max_mins = max(minutes)
        max_guard = guard

print(sleep[max_guard].index(max_mins) * max_guard)
