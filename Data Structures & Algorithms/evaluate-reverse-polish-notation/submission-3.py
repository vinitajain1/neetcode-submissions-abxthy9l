class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i=='+':
                a,b = stack.pop(),stack.pop()
                res = b+a
                stack.append(res)
            elif i=='-':
                a,b = stack.pop(),stack.pop()
                res = b-a
                stack.append(res)
            elif i=='*':
                a,b = stack.pop(),stack.pop()
                res = b*a
                stack.append(res)
            elif i=='/':
                a,b = stack.pop(),stack.pop()
                res = int(float(b)/a)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]