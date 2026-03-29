class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxVol = 0
        while(l<r):
            currHeight = min(heights[l],heights[r])*(r-l)
            maxVol = max(maxVol,currHeight)
            if(heights[l]<heights[r]):
                l=l+1
            else:
                r=r-1
        return maxVol
        