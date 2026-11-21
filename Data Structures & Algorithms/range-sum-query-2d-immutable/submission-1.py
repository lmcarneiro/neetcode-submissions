class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for row in matrix:
            total = 0
            prefix = []
            for n in row:
                total += n
                prefix.append(total)
            self.prefix.append(prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                total += self.prefix[row][col2] - self.prefix[row][col1 - 1]
            else:
                total += self.prefix[row][col2]
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)