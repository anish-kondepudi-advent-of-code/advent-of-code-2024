
class Solution:

    def __init__(self, pathToMatrix):
        with open(pathToMatrix) as file:
            self.matrix = [row.rstrip() for row in file]

    def inBounds(self, rowIdx, colIdx):
        return 0 <= rowIdx < len(self.matrix) and 0 <= colIdx < len(self.matrix[0])
    
    def isXmasCross(self, rowIdx, colIdx):
        if self.matrix[rowIdx][colIdx] != 'A':
            return 0

        topLeft = (rowIdx - 1, colIdx + 1)
        topRight = (rowIdx + 1, colIdx + 1)
        bottomLeft = (rowIdx - 1, colIdx - 1)
        bottomRight = (rowIdx + 1, colIdx - 1)

        for ri, ci in [topLeft, topRight, bottomLeft, bottomRight]:
            if not self.inBounds(ri, ci):
                return 0
            
        word1 = self.matrix[topLeft[0]][topLeft[1]] + self.matrix[rowIdx][colIdx] + self.matrix[bottomRight[0]][bottomRight[1]]
        word2 = self.matrix[topRight[0]][topRight[1]] + self.matrix[rowIdx][colIdx] + self.matrix[bottomLeft[0]][bottomLeft[1]]

        if word1 in ("MAS", "SAM") and word2 in ("MAS", "SAM"):
            return 1
        
        return 0
    
    def solve(self):
        answer = 0
        for rowIdx in range(len(self.matrix)):
            for colIdx in range(len(self.matrix[0])):
                answer += self.isXmasCross(rowIdx, colIdx)
        return answer

solution = Solution("input.txt")
answer = solution.solve()
print(answer)