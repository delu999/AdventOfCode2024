sum = 0

with open("./day2/input.txt", "r") as file:
    for row in file:
        r = row.split(" ")
        arr = [int(str) for str in r]
        
        ok = True
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i] and arr[i]-arr[i-1] < 4 and arr[i]-arr[i-1] > 0:
                continue
            
            ok = False
            break
        
        if not ok:
            ok = True
            for i in range(1, len(arr)):
                if arr[i-1] > arr[i] and arr[i-1]-arr[i] < 4 and arr[i-1]-arr[i] > 0:
                    continue
                ok = False
                break
            
        if ok:
            sum += 1

print(sum)