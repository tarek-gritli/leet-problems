// Runtime: 40ms, Beats 84.62% of users with C++
// Memory: 43.65MB, Beats 38.15% of users with C++

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n=nums.size();
        bool present[100002]={false};
        for(int i=0;i<n;i++)
            if (nums[i]>0 && nums[i]<=100001) present[nums[i]]=true;
        for(int i=1;i<100002;i++)
            if (present[i] == false) return i;
        return 1;
    }
};