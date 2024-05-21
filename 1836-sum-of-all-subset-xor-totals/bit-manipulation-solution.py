# Runtime: 76ms, Beats 27.35% of users with Python3
# Memory: 16.54MB, Beats 48.32% of users with Python3

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        s=0
        for i in range(1 << n):
            xor = 0
            for j in range(n):
                if (i & (1 << j)) != 0:
                    xor ^= nums[j]
            s+=xor
        return s
        