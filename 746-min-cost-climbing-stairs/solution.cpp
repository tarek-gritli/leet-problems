// Runtime: 3ms, Beats 80.13% of users with Python3
// Memory: 16.35MB, Beats 37.07% of users with Python3

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n=cost.size();
        vector<int> dp(n);
        for (int i=0;i<n;i++)
        {
            if (i<2) dp[i] = cost[i];
            else {
                dp[i] = cost[i] + min(dp[i-1],dp[i-2]);
            }
        }
        return min(dp[n-1],dp[n-2]);
    }
};
        
                
