firstList = []
secondList = []

with open("./day1/input.txt", "r") as file:
    for row in file:
        split = row.split(" ")
        firstList.append(int(split[0]))
        secondList.append(int(split[3]))
        
firstList.sort()
secondList.sort()
sum = occ = i = 0

for a in firstList:
    for j in range(0, len(secondList)):
        if a == secondList[j]:
            occ += 1
            i = j
            break
    
    while a == secondList[i+occ]:
        occ += 1

    sum += a * occ
    occ = 0

print(sum)