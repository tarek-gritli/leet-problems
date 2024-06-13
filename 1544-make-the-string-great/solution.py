# Runtime: 37ms, Beats 61.14% of users with Python3
# Memory: 16.50MB, Beats 37.17% of users with Python3

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1]!=s[i] and stack[-1].lower() == s[i].lower():
                stack.pop()
            else:
                stack.append(s[i])
        ch=""
        while stack:
            ch = stack[-1] + ch
            stack.pop()
        return ch