# Runtime: 28ms, Beats 97.18% of users with Python3
# Memory: 16.60MB, Beats 91.49% of users with Python3

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        n=len(strs)
        mini=201
        root=""
        for i in range(n):
            if len(strs[i])<mini:
                mini=len(strs[i])
                root=strs[i]
        for i in range(mini):
            for j in range(n):
                if strs[j][i] != root[i]:
                    return prefix
            prefix+=root[i]
        return prefix