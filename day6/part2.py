def add_to_visited(visited, key):
    if key in visited:
        visited[key] += 1
    else:
        visited[key] = 1

with open("./day6/input.txt", "r") as f:
    fileRows = f.readlines()

rows = len(fileRows)
cols = len(fileRows[0].strip())

saveR, saveC = None, None
for i in range(rows):
    for j in range(cols):
        if fileRows[i][j] == "^":
            saveR, saveC = i, j
            break
    if saveR is not None:
        break

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

path = set()
r, c = saveR, saveC
dir = 0

while 0 <= r < rows and 0 <= c < cols:
    path.add((r, c))
    move = directions[dir]
    nr = r + move[0]
    nc = c + move[1]

    if not (0 <= nr < rows and 0 <= nc < cols):
        break

    if fileRows[nr][nc] == "#":
        dir = (dir + 1) % 4
        continue

    r = nr
    c = nc

path.discard((saveR, saveC))
sum = 0

def simulate_with_obstacle(obstacle):
    r, c = saveR, saveC
    dir = 0
    visited = {}
    add_to_visited(visited, (r, c, dir))

    while 0 <= r < rows and 0 <= c < cols:
        move = directions[dir]
        nr = r + move[0]
        nc = c + move[1]

        if not (0 <= nr < rows and 0 <= nc < cols):
            return False

        if (nr, nc) == obstacle or fileRows[nr][nc] == "#":
            dir = (dir + 1) % 4
            continue

        r = nr
        c = nc
        add_to_visited(visited, (r, c, dir))

        if visited[(r, c, dir)] > 1:
            return True

    return False

for e in path:
    if simulate_with_obstacle(e):
        sum += 1

print(sum)
