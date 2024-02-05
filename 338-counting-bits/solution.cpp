// Runtime: 0ms, Beats 100.00% of users with c++
// Memory: 8.98MB, Beats 33.85% of users with c++

class Solution {
    public:
        vector<int> countBits(int n) {
            vector<int> v(n+1);
            for(int i=0;i<=n;i++)
            {
                v[i]=__builtin_popcount(i);
            }
            return v;
        }
};