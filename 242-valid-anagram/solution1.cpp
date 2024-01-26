// Runtime: 11 ms, faster than 43.26% of C++ online submissions for Contains Duplicate.
// Memory: 9.64 MB, Beats 5.67% of users with C++

class Solution {
public:
    bool isAnagram(string s, string t) {
        int n1=s.length();
        int n2=t.length();
        if(n1!=n2) return false;
        map<char,int> m;
        for(int i=0;i<n1;i++)
        {
            m[s[i]]++;
            m[t[i]]--;
        }
        for(auto el:m)
        {
            if(el.second!=0) return false;
        }
        return true;
        
    }
};