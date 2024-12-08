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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for antenna in antennasWithPos:
    positions = list(antennasWithPos[antenna]) 
    posLen = len(positions)
    while posLen > 0:
        posLen -= 1
        e = positions[posLen]
        unique.add(e)
        for a in positions[:posLen]: 
            pDown, pUp = (a, e) if e[0] > a[0] else (e, a)
            unique.add(a)

            dx_total = pUp[0] - pDown[0]
            dy_total = pUp[1] - pDown[1]
            g = gcd(abs(dx_total), abs(dy_total))
            if g == 0: 
                g = 1

            memDist = (abs(dx_total)//g, abs(dy_total)//g)
            distance = memDist

            if pUp[1] > pDown[1]:
                while True:
                    antinode1 = (pUp[0] + distance[0], pUp[1] + distance[1])
                    if antinode1[0] < rows and 0 <= antinode1[1] < cols:
                        unique.add(antinode1)
                    else:
                        break
                    distance = (distance[0]+memDist[0], distance[1]+memDist[1])
                distance = memDist
                while True:
                    antinode2 = (pDown[0] - distance[0], pDown[1] - distance[1])
                    if antinode2[0] >= 0 and 0 <= antinode2[1] < cols:
                        unique.add(antinode2)
                    else:
                        break
                    distance = (distance[0]+memDist[0], distance[1]+memDist[1])
            else:
                while True:
                    antinode1 = (pUp[0] + distance[0], pUp[1] - distance[1])
                    if antinode1[0] < rows and 0 <= antinode1[1] < cols:
                        unique.add(antinode1)
                    else:
                        break
                    distance = (distance[0]+memDist[0], distance[1]+memDist[1])
                distance = memDist
                while True:
                    antinode2 = (pDown[0] - distance[0], pDown[1] + distance[1])
                    if antinode2[0] >= 0 and 0 <= antinode2[1] < cols:
                        unique.add(antinode2)
                    else:
                        break
                    distance = (distance[0]+memDist[0], distance[1]+memDist[1])

print(len(unique))
