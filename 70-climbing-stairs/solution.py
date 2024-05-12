# Runtime: 29ms, Beats 87.54% of users with Python3
# Memory: 16.62MB, Beats 5.07% of users with Python3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2,n+1):
            calc = prev+curr
            prev = curr
            curr = calc
        return curr 
        
        