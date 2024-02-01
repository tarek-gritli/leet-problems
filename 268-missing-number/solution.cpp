// Runtime: 7ms, Beats 98.02% of users with c++
// Memory: 20.38MB, Beats 16.53% of users with c++

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int given_sum=0;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
            given_sum+=nums[i];
        }
        return n*(n+1)/2 - given_sum;
    }
};