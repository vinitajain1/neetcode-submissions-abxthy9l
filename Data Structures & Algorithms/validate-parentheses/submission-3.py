class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch==')':
                if stack and stack[-1]!='(' or not stack:
                    return False
                if stack:
                    stack.pop()
                continue
            if ch=='}':
                if stack and stack[-1]!='{' or not stack:
                    return False
                if stack:
                    stack.pop()
                continue 
            if ch==']':
                if stack and stack[-1]!='[' or not stack:
                    return False
                if stack:
                    stack.pop()
                continue
            else:
                stack.append(ch)
        return True if not stack else False