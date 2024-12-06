import re

with open("./day3/input.txt", "r") as file:
    matches = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", file.read())
    enabled = True
    sum = 0
    
    for i in matches:
        if i == "do()":
            enabled = True
        elif i == "don't()":
            enabled = False
        else:
            m = re.match(r"mul\((\d+),(\d+)\)", i)
            if m and enabled:
                sum += int(m.group(1)) * int(m.group(2))
                
    print(sum)
