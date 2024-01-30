# Runtime: 117ms, Beats 38.46% of users with Python3
# Memory: 18.54MB, Beats 67.10% of users with Python3

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxLeft=[0]*n
        maxRight=[0]*n
        water=0
        maxi=0
        quantity=0
        for i in range(n):
            maxLeft[i]=maxi
            maxi=max(height[i],maxi)
        maxi=0
        for i in range(n-1,-1,-1):
            maxRight[i]=maxi
            maxi=max(height[i],maxi)
        for i in range(n):
            quantity=min(maxLeft[i],maxRight[i])-height[i]
            water+=max(quantity,0)
        return water
