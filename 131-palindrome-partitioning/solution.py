# Runtime: 478ms, Beats 32.92% of users with Python3
# Memory: 35.13MB, Beats 66.65% of users with Python3

class Solution:
    def palindrome(self,s,i,j):
        while i<j and s[i]==s[j]:
            i+=1
            j-=1
        return i >= j
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, part):
            if i == len(s):
                res.append(part[:])
                return
            for j in range(i,len(s)):
                if self.palindrome(s,i,j):
                    dfs(j+1, part+[s[i:j+1]])
        dfs(0,[])
        return res