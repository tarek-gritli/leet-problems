# Runtime: 104ms, Beats 93.83% of users with Python3
# Memory: 17.81MB, Beats 64.73% of users with Python3

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return n*(n+1)//2 - sum(nums)