import time
start = time.time()
with open("./day7/input.txt", "r") as f:
    file = f.readlines()

maxOp = 0
for i, line in enumerate(file):
    blank_spaces = len(line.split(" ")) - 2
    if (blank_spaces > maxOp):
        maxOp = blank_spaces
print(maxOp)
a = 1
maxPerm = 2 ** maxOp
permutations = [[0 for _ in range(maxOp)] for _ in range(maxPerm)]

for i in range(maxOp-1, -1, -1):
    b = a
    a *= 2
    for j in range(maxPerm):
        permutations[j][i] = "+" if j % a < b else "*"

tot = 0
for _, line in enumerate(file):
    operands = line.split(" ")
    blank_spaces = len(operands) - 2
    totPerm = 2 ** blank_spaces
    for i in range(totPerm):
        tmpTot = int(operands[1])
        for j in range(blank_spaces):
            if permutations[i][j] == "+":
                tmpTot = tmpTot + int(operands[j+2])
            else:
                tmpTot = tmpTot if tmpTot != 0 else 1
                tmpTot = tmpTot * int(operands[j+2])
    
        if int(operands[0][:-1]) == tmpTot:
            tot += tmpTot
            break
print(tot)
end = time.time()
print(end - start)