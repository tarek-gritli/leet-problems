# Runtime: 30ms, Beats 90.04% of users with Python3
# Memory: 16.52MB, Beats 61.96% of users with Python3

class Solution:
    def numSteps(self, s: str) -> int:
        lis = list(s)
        count = 0
        while len(lis) > 1:
            l = len(lis)
            if lis[l - 1] == "0":
                lis.pop()
            else:
                i = len(lis) - 1

                while i >= 0 and lis[i] != "0":
                    lis[i] = "0"
                    i -= 1
                if i < 0:
                    lis.insert(0, "1")
                else:
                    lis[i] = "1"
            count += 1
        return count