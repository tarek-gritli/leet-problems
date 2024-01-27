// Runtime: 16ms, Beats 74.55% of users with C++
// Memory: 27.33MB, Beats 7.18% of users with C++

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int>prefix(n);
        vector<int> postfix(n);
        vector<int> res(n);
        for(int i=0;i<n;i++)
        {
            if(i==0) prefix[i]=nums[i];
            else prefix[i]=nums[i]*prefix[i-1];
        }
        for(int i=n-1;i>=0;i--)
        {
            if(i==n-1) postfix[i]=nums[i];
            else postfix[i]=nums[i]*postfix[i+1];
        }
        for(int i=0;i<n;i++)
        {
            if(i==0) res[i]=postfix[i+1];
            else if(i==n-1) res[i]=prefix[i-1];
            else res[i]=prefix[i-1]*postfix[i+1];
        }
        return res;
    }
};