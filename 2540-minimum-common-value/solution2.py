# Runtime: 335ms, Beats 94.06% of users with Python3
# Memory: 47.04MB, Beats 5.87% of users with Python3

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s=set(nums1)-set(nums2)
        for i in range(len(nums1)):
            if nums1[i] not in s:
                return nums1[i]
        return -1