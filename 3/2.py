import re

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    matches = []
    for i, line in enumerate(lines):
        dos = re.finditer(r"do()", line)
        donts = re.finditer(r"don't()", line)
        muls = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        newMatches = [(i, x.start(0), "start") for x in dos] \
            + [(i, x.start(0), "stop") for x in donts] \
            + [(i, x.start(0), str(x.group())) for x in muls]
        matches += newMatches
    matches.sort()
    
    answer = 0
    start = True
    for _, _, match in matches:
        if match == "start":
            start = True
            continue

        if match == "stop":
            start = False
            continue
        
        if start:
            num1 = int(match.split(",")[0][4:])
            num2 = int(match.split(",")[1][:-1])
            answer += num1 * num2

    print(answer)
