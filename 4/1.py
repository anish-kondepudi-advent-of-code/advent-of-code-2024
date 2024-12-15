
class Solution:

    def __init__(self, wordToFind, pathToMatrix):
        self.WordToFind = wordToFind
        with open(pathToMatrix) as file:
            self.matrix = [row.rstrip() for row in file]

    def inBounds(self, rowIdx, colIdx):
        return 0 <= rowIdx < len(self.matrix) and 0 <= colIdx < len(self.matrix[0])
    
    def getNumberOfWordsToFind(self, rowIdx, colIdx):
        directions = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
        numWordsFound = 0
        for dRow, dCol in directions:
            for i in range(len(self.WordToFind)):
                nRow = rowIdx + dRow * i
                nCol = colIdx + dCol * i
                if not self.inBounds(nRow, nCol):
                    break
                if self.matrix[nRow][nCol] != self.WordToFind[i]:
                    break
                if i == len(self.WordToFind) - 1:
                    numWordsFound += 1
        return numWordsFound
    
    def solve(self):
        answer = 0
        for rowIdx in range(len(self.matrix)):
            for colIdx in range(len(self.matrix[0])):
                answer += self.getNumberOfWordsToFind(rowIdx, colIdx)
        return answer

solution = Solution("XMAS", "input.txt", )
answer = solution.solve()
print(answer)