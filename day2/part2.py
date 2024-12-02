sum = 1

with open("./day2/input.txt", "r") as file:
    for row in file:
        r = row.split(" ")
        arr = [int(str) for str in r]      
        ok = True
        bad = 1
        i = 0
        ord = 0
        while i < len(arr)-1:
            i += 1 
            if arr[i-1] < arr[i] and arr[i]-arr[i-1] < 4 and arr[i]-arr[i-1] > 0:
                ord += 1
                continue
            bad -= 1
            
            if bad >= 0:
                continue
            
            ok = False
            break
        
        arr = [int(str) for str in r]  
        
        if not ok and ord < 2:
            ok = True
            bad = 1
            i = 0
            prec = 0
            while i < len(arr)-1:
                i += 1 
                if arr[i-1] > arr[i] and arr[i-1]-arr[i] < 4 and arr[i-1]-arr[i] > 0:
                    continue
                
                bad -= 1
                if bad >= 0:
                    arr.remove(arr[i])
                    i -= 1
                    continue
                
                ok = False
                break
            
        if ok:
            sum += 1

print(sum)