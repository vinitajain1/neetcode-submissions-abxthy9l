class Solution:
    def trap(self, height: List[int]) -> int:
        # monotonically decreasing stack
        stack=[]
        water = 0
        for r in range(0,len(height)):
            # if not stack or height[stack[-1]]>=height[r]:
            #     stack.append(r)
            while stack and height[stack[-1]]<height[r]:
                top = stack.pop()
                if not stack:
                    continue
                nextTop = stack[-1]
                h = min(height[nextTop],height[r])-height[top]
                w = r-nextTop-1
                water+=w*h
            stack.append(r)
        return water

