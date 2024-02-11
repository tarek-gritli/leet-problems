// Runtime: 8ms, Beats 69.04% of users with C++
// Memory: 12.61MB, Beats 20.59% of users with C++

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> mp = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
        };
        int n=s.length();
        int sum=0;
        for(int i=0;i<n;i++)
        {
            if(i<n-1 && mp[s[i]]<mp[s[i+1]])
            {
                sum-=mp[s[i]];
            }
            else
            {
                sum+=mp[s[i]];
            }
        }
        return sum;
    }
};