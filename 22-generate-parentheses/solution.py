# Runtime: 31ms, Beats 91.46% of users with Python3
# Memory: 16.82MB, Beats 42.61% of users with Python3

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(opening,closing,ch):
            if opening == closing == n:
                res.append(ch)
                return 
            if opening < n :
                gen(opening+1,closing,ch+'(')
            if closing < opening: 
                gen(opening,closing+1,ch+')')
        
        res = []
        gen(0,0,'')
        return res