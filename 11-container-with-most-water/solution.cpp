// Runtime: 65ms, Beats 75.97% of users with C++
// Memory: 61.24MB, Beats 14.00% of users with C++

class Solution {
public:
    int maxArea(vector<int>& height) {
        int h,maxi=0;
        int p=0,q=height.size()-1;
        while(p<q)
        {
            h=min(height[p],height[q])*(q-p);
            maxi=max(maxi,h);
            if(height[p]>height[q]) q--;
            else p++;
        }
        return maxi;
    }
};