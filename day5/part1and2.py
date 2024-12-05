fileRows = []
with open("./day5/input.txt", "r") as f:
    fileRows = f.readlines()

ordList = []
for row in fileRows:
    e = row.split("|")
    if(e[0] == "\n"):
        break
    ordList.append(100 * int(e[0]) + int(e[1]))
ordList.sort(reverse=True)

def part1():
    sum = 0
    for row in reversed(fileRows):
        e = row.split(",")
        if(e[0] == "\n"):
            break

        add = True
        for i in range(len(e)-1):
            if (100 * int(e[i]) + int(e[i+1])) not in ordList:
                add = False
                break

        if add:
            sum += int(e[int(len(e)/2)])
    return sum

def part2():
    sum = 0
    for row in reversed(fileRows):
        e = row.split(",")
        if(e[0] == "\n"):
            break

        add = False
        for i in range(len(e)-1):
            if (100 * int(e[i]) + int(e[i+1])) not in ordList:
                add = True
                break
        
        if not add:
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
        sum += int(e[int(len(e)/2)])

    return sum


print(part1())
print(part2())