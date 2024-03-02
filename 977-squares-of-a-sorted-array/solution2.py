# Runtime: 150ms, Beats 83.29% of users with Python3
# Memory: 18.49MB, Beats 92.99% of users with Python3

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])
            