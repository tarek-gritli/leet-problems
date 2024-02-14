// Runtime: 1469ms, Beats 5.00% of users with C++
// Memory: 62.62MB, Beats 96.74% of users with C++

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k==0) return false;
        int n=nums.size();
        if (n<=k)
        {
            for(int i=0;i<n;i++)
            {
                for(int j=i+1;j<n;j++)
                {
                    if (nums[i]==nums[j]) return true;
                }
            }
            return false;
        }
        for(int i=0;i<n-1;i++)
        {
            for(int j=i+1;j<min(i+k+1,n);j++)
            {
                if (nums[i]==nums[j]) return true;
            }
        }
        return false;
    }
};