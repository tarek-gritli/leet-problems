// Runtime: 52ms, Beats 98.72% of users with C++
// Memory: 26.84MB, Beats 50.62% of users with C++

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n=nums.size();
        vector<vector<int>> res;
        sort(nums.begin(),nums.end());
        for(int i=0;i<n-2;i++)
        {
            if(i>0 && nums[i]==nums[i-1]) continue;
            int j=i+1,k=n-1,total;
            while(j<k)
            {
                total=nums[i]+nums[j]+nums[k];
                if(total>0) k--;
                else if(total<0) j++;
                else
                {
                    res.push_back({nums[i],nums[j],nums[k]});
                    j++;
                    k--;
                    while(j<k && nums[j]==nums[j-1]) j++;
                }
            }

        }
        return res;
    }
};