# Runtime: 36ms, Beats 69.75% of users with Python3
# Memory: 16.46MB, Beats 96.65% of users with Python3

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)