with open("./day6/input.txt", "r") as f:
    fileRows = f.readlines()

#get position of ^
rows = len(fileRows)
cols = len(fileRows[0]) - 1
for i in range(rows):
    for j in range(cols):
        if fileRows[i][j] == "^":
            r = i
            c = j
            break

dir = 0
sum = 1
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
visited = set()
while r+1<rows and r>=0 and c+1<cols and c >= 0:
    if (r,c) not in visited:
        visited.add((r,c))
        sum += 1
    
    move = directions[dir]
    if fileRows[r+move[0]][c+move[1]] == "#":
        dir = (dir + 1) % 4  
        continue
    r += move[0]
    c += move[1]
print(sum)