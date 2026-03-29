class Solution:
    def trap(self, height: List[int]) -> int:
        stack = deque()
        total = 0
        if(len(height)==0):
            return 0
        for i in range(len(height)):
            while stack and height[stack[-1]]<height[i]:
                height_peek = stack[-1]
                stack.pop()
                if not stack:
                    break;
                h = abs(min(height[i],height[stack[-1]])-height[height_peek])
                w = i - stack[-1] - 1
                total = total + (h*w)
            stack.append(i) 
        return total



        