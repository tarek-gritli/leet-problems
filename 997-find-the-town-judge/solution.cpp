// Runtime: 101ms, Beats 98.55% of users with C++
// Memory: 64.30MB, Beats 62.99% of users with C++;

class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> people(n+1);
        for(int i=0;i<trust.size();i++)
        {
            people[trust[i][0]]=1;
        }
        int judge;
        for(int i=1;i<=n;i++)
        {
            if (people[i] == 0)
            {
                judge=i;
                break;
            }
        }
        int count = 0;
        for(int i=0;i<trust.size();i++)
        {
            if(trust[i][1]==judge) count++;
        }
        if(count == n-1) return judge;
        else return -1;
    }
};