// Runtime: 10ms, Beats 73.81% of users with C++
// 13.14MB, Beats 19.64% of users with C++

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        queue<char> q;
        set<char> se;
        int n=s.length();
        int maxi=0;
        for(int i=0;i<n;i++)
        {
            if(se.find(s[i]) == se.end())
            {
                se.insert(s[i]);
                q.push(s[i]);
            }
            else
            {
                maxi=max(maxi,(int)q.size());
                while(!q.empty() && q.front()!=s[i])
                {
                    se.erase(q.front());
                    q.pop();
                }
                if(q.front()==s[i])
                {
                    q.pop();
                    q.push(s[i]);
                }
            }
        }
        return max(maxi,(int)q.size());
    }
};