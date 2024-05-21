# Runtime: 33ms, Beats 80.68% of users with Python3
# Memory: 16.76MB, Beats 30.01% of users with Python3

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(1 << len(nums)):
            sub = []
            for j in range(len(nums)):
                if (i & (1 << j)) != 0:
                    sub.append(nums[j])
            subsets.append(sub)
        return subsets