with open("./day8/input.txt", "r") as f:
    file = f.readlines()

antennasWithPos = {}

for i, fileRow in enumerate(file):
    for j, char in enumerate(fileRow):
        if char == "." or char == "\n": 
            continue
        if char not in antennasWithPos:
            antennasWithPos.update({char: set()})     
        antennasWithPos[char].add((i, j)) 

rows, cols = i+1, j+1
unique = set()
tot = 0
for antenna in antennasWithPos:
    positions = antennasWithPos[antenna] 
    posLen = len(positions)
    while posLen > 0:
        posLen -= 1
        e = positions.pop()
        for a in positions: 
            pDown, pUp = (a, e) if e[0] > a[0] else (e, a)
            distance = (abs(e[0] - a[0]), abs(e[1] - a[1]))
            
            if pUp[1] > pDown[1]:
                antinode1 = (pUp[0] + distance[0], pUp[1] + distance[1])
                antinode2 = (pDown[0] - distance[0], pDown[1] - distance[1])
            else: 
                antinode1 = (pUp[0] + distance[0], pUp[1] - distance[1])
                antinode2 = (pDown[0] - distance[0], pDown[1] + distance[1])

            if antinode1[0] < rows and 0 <= antinode1[1] < cols:
                unique.add(antinode1)

            if antinode2[0] >= 0 and 0 <= antinode2[1] < cols:
                unique.add(antinode2)

print(unique)
print(len(unique))