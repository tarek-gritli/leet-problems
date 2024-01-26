// Runtime: 10 ms, faster than 49.08% of C++ online submissions for Contains Duplicate.
// Memory: 8.59 MB, Beats 5.67% of users with C++

class Solution {
public:
    bool isAnagram(string s, string t) {
        int n1=s.length();
        int n2=t.length();
        if(n1!=n2) return false;
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        if(s>t || s<t) return false;
        return true;
        
    }
};