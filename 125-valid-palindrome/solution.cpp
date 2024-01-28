// Runtime: 0ms, Beats 100.00% of users with C++
// Memory: 8.60MB, Beats 13.78% of users with C++

class Solution {
public:
    bool isPalindrome(string s) {
        int p=0;
        int q=s.length()-1;
        while(p<q)
        {
            while(!isalnum(s[p]) && p<q) p++;
            while(!isalnum(s[q]) && p<q) q--;
            if(tolower(s[p])!=tolower(s[q])) return false;
            p++;
            q--;
        }
        return true;
    }
};