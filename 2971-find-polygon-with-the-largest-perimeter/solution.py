# Runtime: 564ms, Beats 33.50% of users with Python3
# Memory: 31.45MB, Beats 97.32% of users with Python3

class Solution:
    def largestPerimeter(self, nums):
        nums.sort()
        pref=0
        res=-1
        n=len(nums)
        for i in range(n):
            if pref > nums[i]:
                res=pref+nums[i]
            pref+=nums[i]
        return res