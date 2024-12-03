import re


with open("./day3/input.txt", "r", encoding="utf-8") as file:
    matches = re.findall(r"mul[(](\d+),(\d+)[)]", file.read())
    sum = 0
    for e in matches:
        sum += int(e[0]) * int(e[1])
    print(sum)
