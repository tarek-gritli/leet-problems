# Runtime: 36ms, Beats 87.93% of users with Python3
# Memory: 16.53MB, Beats 59.05% of users with Python3

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n= len(grid[0])
        for i in range(m):
            if grid[i][0] == 1:
                continue
            for j in range(n):
                grid[i][j] = 1 if grid[i][j] == 0 else 0
        for i in range(1,n):
            if self.count_ones(grid, i, m) > m//2:
                continue
            for j in range(m):
                grid[j][i] = 1 if grid[j][i] == 0 else 0
        s=0
        for i in range(m):
            s+=self.helper(grid[i])
        return s
    def helper(self,l):
        ch = ''.join(str(elem) for elem in l)
        return int(ch,2)
    def count_ones(self,grid,i, m):
        ones = 0
        for j in range(m):
            if grid[j][i] == 1:
                ones+=1
        return ones 

