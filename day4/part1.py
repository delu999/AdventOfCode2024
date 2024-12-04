import re

def findXMAS(string):
    return re.findall(r"(?=(XMAS))|(?=(SAMX))", string)

with open("./day4/input.txt", "r") as f:
    arr = f.readlines()
    cols = len(arr[0]) - 1
    sum = 0
    
    for row in arr:   #horizontal
        sum += len(findXMAS(row))
    
    for col in range(0, cols):   #vertical
        ver = ""
        for row in arr:
            ver += row[col]

        sum += len(findXMAS(ver))   

    diagNum = 1  # diagonal r to l, top half
    while diagNum < cols-2:
        r = 0
        diag = ""
        while r < len(arr)-diagNum:
            diag += arr[r][r+diagNum]
            r += 1
        
        diagNum += 1
        sum += len(findXMAS(diag))

    
    diagNum = 0  # diagonal r to l, bottom half
    while diagNum < cols:
        r = 0
        diag = ""
        while r < len(arr)-diagNum:
            diag += arr[r+diagNum][r]
            r += 1

        diagNum += 1
        
        sum += len(findXMAS(diag))

    
    diagNum = 0
    tmpCols = cols
    while diagNum < cols-2: # diagonal l to r, top half
        r = 0
        diag = ""

        while r < len(arr)-diagNum:
            diag += arr[r][tmpCols-r-1]
            r += 1

        diagNum += 1
        tmpCols -= 1
        sum += len(findXMAS(diag))

    
    diagNum = 1
    while diagNum < cols-2: # diagonal l to r, bottom half
        r = diagNum
        j = 0
        diag = ""

        while r < len(arr):
            diag += arr[r][cols-1-j]
            r += 1
            j += 1

        diagNum += 1
        sum += len(findXMAS(diag))

    
                    
    print(sum)

        

       