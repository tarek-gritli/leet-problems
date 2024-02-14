# Runtime: 41ms, Beats 80.64% of users with Python3
# Memory: 16.78MB, Beats 80.43% of users with Python3

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        n=len(operations)
        l=0
        for i in range(n):
            if operations[i]=="C":
                res.pop()
                l-=1
            elif operations[i]=="D":
                res.append(res[l-1]*2)
                l+=1
            elif operations[i]=="+":
                res.append(res[l-1]+res[l-2])
                l+=1
            else:
                res.append(int(operations[i]))
                l+=1
        return sum(res)
            