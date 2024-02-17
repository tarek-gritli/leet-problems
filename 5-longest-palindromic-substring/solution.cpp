// Runtime: 8ms, Beats 92.46% of users with C++
// Memory: 8.08MB, Beats 76.44% of users with C++


class Solution {
public:
    string longestPalindrome(string s) {
        int n=s.size();
        int maxi=0;
        int start=0;
        int l,r;
        string substring="";
        for (int i=0;i<n;i++)
        {
            l=i,r=i;
            while (l>=0 && r<n && s[l] == s[r])
            {
                if (r-l+1 > maxi)
                {
                    start=l;
                    maxi=r-l+1;
                }
                l--;
                r++;
            }
            l=i,r=i+1;
            while (l>=0 && r<n && s[l] == s[r])
            {
                if(r-l+1 > maxi)
                {
                    start=l;
                    maxi=r-l+1;
                }
                l--;
                r++;
            }
        }
        return s.substr(start,maxi);
    }
};