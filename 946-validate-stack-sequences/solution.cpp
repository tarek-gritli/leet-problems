// Runtime: 4ms, Beats 84.60% of users with C++
// Memory: 17.81MB, Beats 70.40% of users with C++

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> st;
        int i = 0, n = pushed.size();
        for(int num : pushed) {
            st.push(num);
            while (!st.empty() && popped[i] == st.top()) {
                st.pop();
                i++;
            }
        }
        return st.empty();
    }
};