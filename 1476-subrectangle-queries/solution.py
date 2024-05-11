# Runtime: 117ms, Beats 96.22% of users with Python3
# Memory: 18.55MB, Beats 66.42% of users with Python3


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1,row2+1):
            self.matrix[i][col1:col2+1]=[newValue]*(col2-col1+1)

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)