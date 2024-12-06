import re

with open("./day3/input.txt", "r") as file:
    fileContent = "do()" + file.read().strip() + "don't()"
    print(fileContent)
    matches = re.findall(r"(?<=do[(][)]).*?mul[(](\d+),(\d+)[)](?=.*?don't[(][)])", fileContent, re.DOTALL)
    sum = 0
    for e in matches:
        sum += int(e[0]) * int(e[1])
    print(sum)
