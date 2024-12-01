firstList = []
secondList = []

with open("./day1/input.txt", "r") as file:
    for row in file:
        split = row.split(" ")
        firstList.append(int(split[0]))
        secondList.append(int(split[3]))
        
firstList.sort()
secondList.sort()
sum = 0

for i in range(0, len(firstList)):
    sum += abs(firstList[i] - secondList[i])

print(sum)