class Solution:
    def trap(self, height: List[int]) -> int:
        maxWater = 0
        stack = []
        for i in range(0,len(height)):
            while stack and height[stack[-1]]<height[i]:
                top = stack.pop()
                if not stack:
                    continue
                nextTop = stack[-1]
                h = min(height[nextTop],height[i]) - height[top]
                w = i-nextTop-1
                maxWater+=h*w
            stack.append(i)
        return maxWater
        