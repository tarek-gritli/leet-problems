// Runtime: 86ms, Beats 84.72% of users with C++
// Memory: 95.69MB, Beats 23.82% of users with C++
//Brute Force will not be efficient and will get you a TLE

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int p=0,q=1,maxi=0,n=prices.size();
        while(q<n)
        {
            if(prices[q]>prices[p]) maxi=max(maxi,prices[q]-prices[p]);
            else p=q;
            q++;
        }
        return maxi;
    }
};