// Runtime: 11ms, Beats 66.15% of users with C++
// Memory: 23.33MB, Beats 5.02% of users with C++

class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        vector<int> maxLeft(n);
        vector<int> maxRight(n);
        int water=0,maxi=0;
        for(int i=0;i<n;i++)
        {
            maxLeft[i]=maxi;
            maxi=max(height[i],maxi);
        }
        maxi=0;
        for(int i=n-1;i>=0;i--)
        {
            
            maxRight[i]=maxi;
            maxi=max(height[i],maxi);
        }
        int quantity;
        for(int i=0;i<n;i++)
        {
            quantity=min(maxLeft[i],maxRight[i]);
            water+=max(0,quantity-height[i]);
        }
        return water;
    }
};