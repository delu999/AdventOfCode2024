tmpFile = open("./day9/input.txt", "r")
diskMap = list(tmpFile.readline())
tmpFile.close()
disk = []
freeSpaceIdxs = [0]
id = 0
bf = {}

for i in range(0, len(diskMap), 2):
    bf.update({id: int(diskMap[i])})
    for j in range(int(diskMap[i])):
        disk.append(id)
        
    if i+1 >= len(diskMap):
        continue

    for j in range(int(diskMap[i+1])):
        disk.append('.')

    id += 1

tot = 0
for i in range(len(disk)-1, 0, -1):
    if disk[i] == '.':
        freeSpaceIdxs.append(i)
        tot += 1 
i = 0
last = 0
for i in range(len(disk)):
    if id == -1:
        break
    if disk[i] != '.':
        continue 

    c = bf[id]
    i -= 1
    while c > 0:
        i += 1
        if i > len(disk)-1:
            break
        if disk[i] != '.':
            continue
        disk[i] = id
        c -= 1
    id -= 1


start = len(disk) - 1
while tot > 0:
    disk[start] = '.'
    start -= 1
    tot -= 1

checksum = 0
id = 0

for id, e in enumerate(disk):
    if e == '.':
        break
    checksum += int(e) * id
