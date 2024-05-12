# Runtime: 64ms, Beats 87.24% of users with Python3
# Memory: 20.08MB, Beats 60.23% of users with Python3

class NumArray:

    def __init__(self, nums: List[int]):
        self.pref=[]
        s = 0
        for num in nums:
            s+=num
            self.pref.append(s)

    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.pref[right]-self.pref[left-1]
        return self.pref[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)