def add_neighbor(paths, next, x, y, count):
    if next not in paths:
        paths[next] = {}
    if (x, y) not in paths[next]:
        paths[next][(x, y)] = 0
    paths[next][(x, y)] += count

def unique_paths(trailHeads, trailMap, rows, cols):
    paths = {}
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    paths[0] = {}
    for head in trailHeads:
        paths[0][head] = 1

    for next in range(1, 10):
        paths[next] = {}
        for (x, y), count in paths[next - 1].items():
            for move in moves:
                r, c = x + move[0], y + move[1]
                if 0 <= r < rows and 0 <= c < cols and trailMap[r][c] == str(next):
                    add_neighbor(paths, next, r, c, count)

    total_paths = sum(paths[9].values()) if 9 in paths else 0
    return total_paths

def part2():
    tmpFile = open("./day10/input.txt", "r")
    trailMap = tmpFile.readlines()
    tmpFile.close()
    rows = len(trailMap)
    cols = len(trailMap[0]) - 1

    trailHeads = set()
    for i in range(rows):
        for j in range(cols):
            if trailMap[i][j] == "0":
                trailHeads.add((i, j))

    return unique_paths(trailHeads, trailMap, rows, cols)

print(part2())
