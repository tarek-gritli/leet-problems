# Runtime: 41ms, Beats 99.03% of users with Python3
# Memory: 16.68MB, Beats 81.98% of users with Python3

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prevprev = cost[0]
        prev = cost[1]
        for i in range (2,n):
            curr = cost[i]+min(prev,prevprev)
            prevprev = prev
            prev = curr
        return min(prev,prevprev)
        
                
