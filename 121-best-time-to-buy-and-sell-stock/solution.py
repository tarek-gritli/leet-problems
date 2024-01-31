# Runtime: 771ms, Beats 65.25% of users with Python3
# Memory: 27.40MB, Beats 83.73% of users with Python3

"""
    -Let's say we're buying on the first day
    -We will iterate through the array to find the maximum profit:
        -If the current price is less than the price we bought at, we will buy at the current price
        -Otherwise, we will sell at the current price and update profit
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if(buy>prices[i]):
                buy=prices[i]
            else:
                maxi=max(maxi,prices[i]-buy)
        return maxi
        
        