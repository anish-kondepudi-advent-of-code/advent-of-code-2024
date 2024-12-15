with open("input.txt") as file:
    lines = [line.rstrip().split() for line in file]
    left, right = [], []

    for i in range(len(lines)):
        left.append(int(lines[i][0]))
        right.append(int(lines[i][1]))

    left.sort()
    right.sort()
    distanceSum = 0

    for i in range(len(left)):
        distanceSum += abs(left[i] - right[i])

    print(distanceSum)