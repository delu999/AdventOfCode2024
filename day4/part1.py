import re

with open("./day4/input.txt", "r") as f:
    arr = f.readlines()
    cols = len(arr[0]) - 1
    sum = 0
    
    for row in arr:   #horizontal
        if (len(re.findall(r"XMAS|SAMX", row))):
            sum += 1

    for col in range(0, cols):   #vertical
        ver = ""
        for row in arr:
            ver += row[col]

        if (len(re.findall(r"XMAS|SAMX", ver))):
            sum += 1
            
    diagNum = 0  # diagonal r to l, top half
    while diagNum < cols:
        r = 0
        diag = ""
        while r < len(arr)-diagNum:
            diag += arr[r][r+diagNum]
            r += 1
        
        diagNum += 1
        
        if (len(re.findall(r"XMAS|SAMX", diag))):
            sum += 1
    
    diagNum = 0  # diagonal r to l, bottom half
    while diagNum < cols:
        r = 0
        diag = ""
        while r < len(arr)-diagNum:
            diag += arr[r+diagNum][r]
            r += 1

        diagNum += 1
        
        if (len(re.findall(r"XMAS|SAMX", diag))):
            sum += 1
    
    diagNum = 0
    tmpCols = cols
    while diagNum < cols+5: # diagonal l to r, top half
        r = 0
        diag = ""

        while r < len(arr)-diagNum:
            diag += arr[r][cols-r-1]
            r += 1

        diagNum +=1
        cols -= 1
        print(diag)
        if (len(re.findall(r"XMAS|SAMX", diag))):
            sum += 1
    
    diagNum = 0
    tmpCols = cols
    while diagNum < cols: # diagonal l to r, top half
        r = 0
        diag = ""

        while r < len(arr)-diagNum:
            diag += arr[r+diagNum][cols-1-diagNum]
            r += 1
        
        diagNum +=1
        cols -= 1
        if (len(re.findall(r"XMAS|SAMX", diag))):
            sum += 1
    
    

                    
    print(sum)

        

       