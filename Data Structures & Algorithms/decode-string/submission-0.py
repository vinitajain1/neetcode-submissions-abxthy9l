class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch=="]":
                currStr = []
                while stack and stack[-1]!="[":
                    currStr.append(stack.pop())
                stack.pop() # remove "["
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                decoded = "".join(reversed(currStr))
                repeat = int("".join(reversed(num)))
                stack.append(decoded*repeat)
            else:
                stack.append(ch)
        return "".join(stack)
