# Runtime: 53ms, Beats 59.76% of users with Python3
# Memory: 16.79MB, Beats 64.63% of users with Python3

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        n=len(tokens)
        score = 0
        maxi = 0
        l,r = 0,n-1
        while l<=r:
            if power>=tokens[l]:
                power-=tokens[l]
                l+=1 
                score+=1
                maxi=max(maxi,score) 
            elif power < tokens[l] and tokens[r]>power:
                if score < 1:
                    break
                power+=tokens[r]
                r-=1
                score-=1
        return maxi