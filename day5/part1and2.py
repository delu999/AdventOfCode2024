fileRows = []
with open("./day5/input.txt", "r") as f:
    fileRows = f.readlines()

ordList = []
pos = 0
for k, row in enumerate(fileRows):
    e = row.split("|")
    if(e[0] == "\n"):
        pos = k+1
        break
    ordList.append(100 * int(e[0]) + int(e[1]))
ordList.sort(reverse=True)

def isSorted(arr):
    add = True
    for i in range(len(arr)-1):
        if (100 * int(arr[i]) + int(arr[i+1])) not in ordList:
            add = False
            break
    return add

def part1():
    sum = 0
    for z in range(pos, len(fileRows)):
        e = fileRows[z].split(",")
        if(e[0] == "\n"):
            break

        if isSorted(e):
            sum += int(e[len(e)//2])
    return sum

def part2():
    sum = 0
    for z in range(pos, len(fileRows)):
        e = fileRows[z].split(",")
        if(e[0] == "\n"):
            break
        
        if isSorted(e):
            continue
        
        for i in range(len(e)-1, 0, -1):        
            swapped = False
            for j in range(i):
                if (100 * int(e[j]) + int(e[j+1])) in ordList:
                    continue
                e[j], e[j + 1] = e[j + 1], e[j]
                swapped = True
            if not swapped:
                break
        sum += int(e[len(e)//2])

    return sum

print(part1())
print(part2())