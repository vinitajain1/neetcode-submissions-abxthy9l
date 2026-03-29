class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prevSmall = [-1]*n
        nextSmall = [n]*n

        # Monotonically increasing stack
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                nextSmall[stack.pop()] = i
            stack.append(i)
        stack = []

        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>heights[i]:
                prevSmall[stack.pop()] = i
            stack.append(i)
        
        maxArea = 0
        print(prevSmall)
        print(nextSmall)
        for i in range(n):
            width = (i - prevSmall[i]) + (nextSmall[i]-i) - 1
            height = heights[i]
            maxArea = max(maxArea,width*height)
        return maxArea


        