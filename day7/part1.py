with open("./day7/input.txt", "r") as f:
    file = f.readlines()

tot = 0
for i, line in enumerate(file):
    operands = line.split(" ")
    result = int(operands[0][:-1])
    blank_spaces = len(operands) - 2
    totPerm = 2 ** blank_spaces
    permutations = [[0 for _ in range(blank_spaces)] for _ in range(totPerm)]
    
    k = 0
    for i in range(blank_spaces-1, -1, -1):
        k += 1
        a = 2 ** k
        b = 2 ** (k-1)
        for j in range(totPerm):
            permutations[j][i] = "+" if j % a < b else "*"

    for i in range(totPerm):
        tmpTot = int(operands[1])
        for j in range(blank_spaces):
            if permutations[i][j] == "+":
                tmpTot = tmpTot + int(operands[j+2])
            else:
                tmpTot = tmpTot if tmpTot != 0 else 1
                tmpTot = tmpTot * int(operands[j+2])
    
        if result == tmpTot:
            tot += result
            break
print(tot)