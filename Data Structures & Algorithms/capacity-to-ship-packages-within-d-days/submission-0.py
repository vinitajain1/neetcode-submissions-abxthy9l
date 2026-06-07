class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ans = 0
        l=max(weights)
        r=sum(weights)
        def ifPossible(leastWt):
            d = 1
            currWt = 0
            for wt in weights:
                currWt+=wt
                if currWt>leastWt:
                    d+=1
                    currWt = wt
            return d<=days
        while l<=r:
            mid = (l+r)//2
            p = ifPossible(mid)
            if p:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans