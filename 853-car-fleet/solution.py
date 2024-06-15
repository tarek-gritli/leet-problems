# Time: 667ms, Beats 71.13% of users with Python3
# Memory: 38.70MB, Beats 50.68% of users with Python3

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        l = sorted(zip(position,speed), reverse=True)
        for i in range(len(l)):
            if stack:
                time = (target-stack[-1][0])/stack[-1][1]
                time2 = (target-l[i][0])/l[i][1]
                if time2>time:
                    stack.append(l[i])
            else:
                stack.append(l[i])
        return len(stack)
