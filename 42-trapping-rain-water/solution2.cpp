// Runtime: 8ms, Beats 80.51% of users with C++
// Memory: 22.40MB, Beats 8.92% of users with C++

class Solution {
public:
    int trap(vector<int>& height) {
        int water=0;
        int p=0,q=height.size()-1;
        int maxLeft=height[p],maxRight=height[q];
        while (p<q)
        {
            if(maxLeft<=maxRight)
            {
                p++;
                maxLeft=max(maxLeft,height[p]);
                water+=maxLeft-height[p];
                
            }
            else
            {
                q--;
                maxRight=max(maxRight,height[q]);
                water+=maxRight-height[q];
            }
        }
        return water;
    }
};