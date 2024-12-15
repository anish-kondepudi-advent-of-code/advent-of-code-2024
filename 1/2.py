with open("input.txt") as file:
    lines = [line.rstrip().split() for line in file]
    left, right = [], []

    for i in range(len(lines)):
        left.append(int(lines[i][0]))
        right.append(int(lines[i][1]))

    similarityScore = 0
    rightCounts = {}

    for num in right:
        if num not in rightCounts:
            rightCounts[num] = 0
        rightCounts[num] += 1

    for num in left:
        if num in rightCounts:
            similarityScore += num * rightCounts[num]
        
    print(similarityScore)