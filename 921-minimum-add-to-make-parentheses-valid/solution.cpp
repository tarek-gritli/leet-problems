// Runtime: 100ms, Beats 100.00% of users with C++
// Memory: 9.09MB, Beats 8.54% of users with C++

class Solution {
public:
    int minAddToMakeValid(string s) {
        ios::sync_with_stdio();cin.tie(NULL);
        stack<char> st;
        for(int i =0;i<s.length();i++) {
            if(s[i] == '(') st.push('(');
            else{
                if(!st.empty() && st.top() == '(') st.pop();
                else st.push(')');
            }
        }
        return st.size();
    }
};