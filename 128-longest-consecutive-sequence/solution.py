# Runtime: 331ms, Beats 96.93% of users with Python3
# Memory: 31.80MB, Beats 73.04% of users with Python3

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxi=0
        for el in nums:
            if el-1 not in nums:
                count=1
                while el+1 in nums:
                    count+=1
                    el=el+1
                if(count>maxi):
                    maxi=count
        return maxi
        
        