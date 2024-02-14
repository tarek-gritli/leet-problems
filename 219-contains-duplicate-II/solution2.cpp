// Runtime: 136ms, Beats 46.63% of users with C++
// Memory: 82.92MB, Beats 12.36% of users with C++

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int n=nums.size();
        set<int> s;
        int i=0;
        for (int j=0;j<n;j++)
        {
            if(j-i>k)
            {
                s.erase(nums[i]);
                i++;
            }
            if (s.find(nums[j])!=s.end()) return true;
            s.insert(nums[j]);
        }
        return false;
    }
};