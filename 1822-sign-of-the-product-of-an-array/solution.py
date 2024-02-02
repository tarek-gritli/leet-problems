# Runtime: 57ms, Beats 75.01% of users with Python3
#Memory: 16.74MB, Beats 64.47% of users with Python3

#To facilitate sum multiply p by -1 if number is negative, return 0 if you find a 0 if you find one in the array
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=1
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                return 0
            elif nums[i]<0:
                p*=-1
        return p