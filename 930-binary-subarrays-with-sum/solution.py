# Runtime: 220ms, Beats 64.54% of users with Python3
# Memory: 17.30MB, Beats 87.31% of users with Python3

class Solution:
    def slide(self,nums,goal):
        if goal < 0:
            return 0
        l=0
        res=0
        curr=0
        for r in range(len(nums)):
            curr+=nums[r]
            while curr>goal:
                curr-=nums[l]
                l+=1
            res+=r-l+1
        return res
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.slide(nums,goal)-self.slide(nums,goal-1)


    