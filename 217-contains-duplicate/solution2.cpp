// Runtime: 90 ms, faster than 80% of C++ online submissions for Contains Duplicate.
// Memory: 60.82 MB, Beats 73.61% of users with C++

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        for(int i=1;i<n;i++)
        {
            if(nums[i]==nums[i-1]) return true;
        }
        return false;
    }
};
