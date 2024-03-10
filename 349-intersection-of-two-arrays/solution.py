# Runtime: 40ms, Beats 92.93% of users with Python3
# Memory: 16.62MB, Beats 91.42% of users with Python3

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))