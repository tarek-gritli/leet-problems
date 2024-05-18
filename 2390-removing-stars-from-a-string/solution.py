# Runtime: 131ms, Beats 72.33% of users with Python3
# Memory: 18.29MB, Beats 62.77% of users with Python3

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*' and stack:
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)
            
            
