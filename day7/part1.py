with open("./day7/input.txt", "r") as f:
    file = f.readlines()

maxOp = 0
for i, line in enumerate(file):
    blank_spaces = len(line.split(" ")) - 2
    if (blank_spaces > maxOp):
        maxOp = blank_spaces

a = 1
totPerm = 2 ** maxOp
permutations = [[] for _ in range(totPerm)]

for i in range(maxOp - 1, -1, -1):
    b = a
    a *= 2
    for j in range(totPerm):
        permutations[j].insert(0, "+" if j % a < b else "*")

tot = 0
for _, line in enumerate(file):
    operands = line.split(" ")
    blank_spaces = len(operands) - 2
    totPerm = 2 ** blank_spaces
    
    for i in range(totPerm):
        tmpTot = int(operands[1])
        k = 1
        for j in range(maxOp - blank_spaces, maxOp):
            k += 1
            if permutations[i][j] == "+":
                tmpTot = tmpTot + int(operands[k])
            else:
                tmpTot = tmpTot if tmpTot != 0 else 1
                tmpTot = tmpTot * int(operands[k])
    
        if int(operands[0][:-1]) == tmpTot:
            tot += tmpTot
            break
print(tot)