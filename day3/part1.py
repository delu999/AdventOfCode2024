import re


with open("./day3/input.txt", "r", encoding="utf-8") as file:
    sum = 0
    matches = re.findall(r"mul[(](\d+),(\d+)[)]", file.read())
    print("Matches:", matches[0][0])
    
    for e in matches:
        sum += int(e[0]) * int(e[1])
