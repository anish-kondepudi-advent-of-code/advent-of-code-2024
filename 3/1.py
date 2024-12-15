import re

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    answer = 0
    for line in lines:
        matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        for match in matches:
            mulStr = str(match.group())
            num1 = int(mulStr.split(",")[0][4:])
            num2 = int(mulStr.split(",")[1][:-1])
            answer += num1 * num2
    print(answer)


