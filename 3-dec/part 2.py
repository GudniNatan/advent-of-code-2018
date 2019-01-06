file = list()
with open("3-dec/input.txt") as file_pointer:
    file.extend(file_pointer)

claims = list()
board_width = 0
board_height = 0

for line in file:
    id_number = int(line.split(" @")[0][1:])
    line = line.split("@ ")[1].split(": ")
    coords = line[0].split(",")
    dimensions = line[1].split("x")
    x = int(coords[0])
    y = int(coords[1])
    w = int(dimensions[0])
    h = int(dimensions[1])
    claims.append({"x": x, "y": y, "w": w, "h": h, "id": id_number})
    board_width = max(x + w, board_width)
    board_height = max(y + h, board_height)

board = [[0 for i in range(board_width + 1)] for j in range(board_height + 1)]

for claim in claims:
    for i in range(claim["w"]):
        for j in range(claim["h"]):
            board[claim["x"] + i][claim["y"] + j] += 1

for claim in claims:
    clean = True
    for i in range(claim["w"]):
        for j in range(claim["h"]):
            if board[claim["x"] + i][claim["y"] + j] != 1:
                clean = False
    if clean:
        print(claim["id"])
