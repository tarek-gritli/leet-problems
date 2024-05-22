# Runtime: 105ms, Beats 68.65% of users with Python3
# Memory: 16.94MB, Beats 5.94% of users with Python3

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,len(nums)-1
        while l<r:
            if nums[r]>-nums[l]:
                r-=1
            elif nums[l]<-nums[r]:
                l+=1
            else:
                return nums[r]
        return -1
