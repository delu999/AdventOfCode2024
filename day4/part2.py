with open("./day4/input.txt", "r") as f: a = f.readlines()
sum = 0

for i in range(len(a)-2):
    for j in range(len(a[0])-2):
        if a[i+1][j+1] != 'A':
            continue
        if a[i][j] == 'M' and a[i][j+2] == 'M' and a[i+2][j] == 'S' and a[i+2][j+2] == 'S':
            sum+=1
        elif a[i][j] == 'S' and a[i][j+2] == 'S' and a[i+2][j] == 'M' and a[i+2][j+2] == 'M':
            sum+=1
        elif a[i][j] == 'M' and a[i][j+2] == 'S' and a[i+2][j] == 'M' and a[i+2][j+2] == 'S':
            sum+=1
        elif a[i][j] == 'S' and a[i][j+2] == 'M' and a[i+2][j] == 'S' and a[i+2][j+2] == 'M':
            sum+=1

print(sum)