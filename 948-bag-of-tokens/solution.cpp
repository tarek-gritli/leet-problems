// Runtime: 0ms, Beats 100.00% of users with C++
// Memory: 13.22MB, Beats 23.53% of users with C++

class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int n=tokens.size();
        sort(tokens.begin(),tokens.end());
        int l=0,r=n-1,score=0,maxi=0;
        while (l<=r)
        {
            if (power>= tokens[l])
            {
                power-=tokens[l];
                score++;
                maxi=max(maxi,score);
                l++;
            }
            else if (power<tokens[l] && power<tokens[r])
            {
                if(score<1) break;
                score--;
                power+=tokens[r];
                r--;
            }
        }
        return maxi;
    }
};