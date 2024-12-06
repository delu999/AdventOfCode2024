with open("./day6/input.txt", "r") as f:
    fileRows = f.readlines()

posRow = posCol = sum = dir = 0
ar = []
for i, row in enumerate(fileRows):
    tmp = []
    for j in range(len(fileRows[0])-1):
        if row[j] == "#":
           tmp.append(4)
           continue
        elif row[j] != ".":
            posRow = i
            posCol = j
        tmp.append(5)     
    ar.append(tmp)

#0=up, 1=right, 2=down, 3=left, 4=#, 5=., 6=visited 
try:    
    while True:
        if ar[posRow][posCol] != 6:
            ar[posRow][posCol] = 6
            sum += 1
        match dir:
            case 0:       
                if ar[posRow-1][posCol] != 4:
                    posRow -= 1        
                else:
                    dir = 1
            case 1:
                if ar[posRow][posCol+1] != 4:
                    posCol += 1        
                else:
                    dir = 2
            case 2:
                if ar[posRow+1][posCol] != 4:
                    posRow += 1
                else:
                    dir = 3
            case 3:
                if ar[posRow][posCol-1] != 4:
                    posCol -= 1
                else:
                    dir = 0      
except:
    print(sum)