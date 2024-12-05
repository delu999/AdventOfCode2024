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

print(sum)