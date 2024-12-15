def isSafe(difference, lineIsIncreasing, lineIsIDecreasing):
    if 1 <= difference <= 3 and lineIsIncreasing:
        return True
    if -3 <= difference <= -1 and lineIsIDecreasing:
        return True
    return False

def isIncreasing(line):
    for i in range(1, len(line)):
        if line[i] - line[i-1] <= 0:
            return False
    return True

def isIDecreasing(line):
    for i in range(1, len(line)):
        if line[i] - line[i-1] >= 0:
            return False
    return True

with open("input.txt") as file:
    lines = [list(map(int, line.rstrip().split())) for line in file]

    numSafeLines = 0
    for line in lines:
        lineIsIncreasing = isIncreasing(line)
        lineIsIDecreasing = isIDecreasing(line)
        lineIsSafe = True
        for i in range(1, len(line)):
            difference = line[i] - line[i-1]
            lineIsSafe &= isSafe(difference, lineIsIncreasing, lineIsIDecreasing) # if at least one level is not safe, the entire line is unsafe
        numSafeLines += lineIsSafe

    print(numSafeLines)