// Runtime: 7ms, Beats 80.97% of users with C++
// Memory: 8.34MB, Beats 27.13% of users with C++

class Solution {
public:
    int characterReplacement(string s, int k) {
        int n=s.length();
        int i=0;
        int res=0;
        int maxf=0;
        vector<int> count(26,0);
        for(int j=0;j<n;j++)
        {
            count[s[j]-'A']++;
            maxf=max(maxf,count[s[j]-'A']);
            while((j-i+1)-maxf>k)
            {
                count[s[i]-'A']--;
                i++;
            }
            res=max(res,j-i+1);
        }
        return res;
    }
};