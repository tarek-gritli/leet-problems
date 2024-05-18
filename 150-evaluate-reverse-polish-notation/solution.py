# Runtime: 64ms, Beats 65.16% of users with Python3
# Memory: 17.14MB, Beats 33.30% of users with Python3

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        i = 0
        while i < n:
            if tokens[i] not in ('+','*','/','-'):
                stack.append(int(tokens[i]))
            if tokens[i] == '+':
                stack.append(stack.pop()+stack.pop())
            elif tokens[i] == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            elif tokens[i] == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif tokens[i] == '*':
                stack.append(stack.pop()*stack.pop())
            i+=1
        return stack[-1]

