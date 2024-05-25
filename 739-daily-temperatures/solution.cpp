// Rutnime: 130ms, Beats 30.97% of users with C++
// Memory: 109.97MB, Beats 10.08% of users with C++

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<pair<int,int>> s;
        vector<int> v(n);
        int j;
        for(int i=0;i<n;i++) {
            while(!s.empty() && temperatures[i] > s.top().first) {  
                j = s.top().second;
                s.pop();
                v[j] = i - j;
            }
            s.push({temperatures[i], i});
        }
        return v;
    }
};