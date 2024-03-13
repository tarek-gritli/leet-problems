# Runtime: 46ms, Beats 60.68% of users with Python3
# Memory: 16.55MB, Beats 59.17% of users with Python3

class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = 1
        x=pivot*(pivot+1)//2
        while pivot <= n:
            if pivot*(pivot+1)//2 == n*(n+1)//2-pivot*(pivot+1)//2 + pivot:
                return pivot
            pivot+=1
        return -1
        