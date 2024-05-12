# Runtime: 131ms, Beats 53.08% of users with Python3
# Memory: 17.06MB, Beats 70.30% of users with Python3

class Solution:
    def matrix_max(self, grid, i, j):
        maxi = 0
        for a in range(i,i+3):
            for b in range(j,j+3):
                maxi = max(grid[a][b],maxi)
        return maxi
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        k = len(grid) - 2
        maxLocal = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                maxLocal[i][j] = self.matrix_max(grid, i, j)
        return maxLocal
