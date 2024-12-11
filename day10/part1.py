def addNeighbor(next, paths, x, y):
    if next not in paths:
        paths.update({next: set()})
    paths[next].add((x, y))    

def findScore(trailHead, trailMap, rows, cols):
    paths = {}
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def f(x, y, next):    
        if next == 10:
            return
        
        for m in moves:
            r, c = x + m[0], y + m[1]
            if 0 <= r < rows and 0 <= c < cols and trailMap[r][c] == str(next): 
                addNeighbor(next, paths, r, c)
        
        if next not in paths:
            return
        
        for e in paths[next]:
            f(e[0], e[1], next+1)
    
    f(trailHead[0],  trailHead[1], 1)
    return len(paths[9]) if 9 in paths else 0


def part1():
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
    
    scores = 0
    while len(trailHeads) > 0:
        scores += findScore(trailHeads.pop(), trailMap, rows, cols)
    return scores
        

print(part1())