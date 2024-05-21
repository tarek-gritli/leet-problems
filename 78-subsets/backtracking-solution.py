# Runtime: 31ms, Beats 90.44% of users with Python3
# Memory: 16.82MB, Beats 8.16% of users with Python3

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i,sub):
            if i == len(nums):
                subsets.append(sub.copy())
                return
            sub.append(nums[i])
            backtrack(i+1,sub)  
            sub.pop()
            backtrack(i+1,sub)

        subsets = []
        backtrack(0,[])
        return subsets