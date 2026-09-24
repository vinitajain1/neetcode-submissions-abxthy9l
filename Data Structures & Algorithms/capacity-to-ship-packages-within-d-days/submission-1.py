class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        def isMinWeightCap(mid):
            daysNeeded = 1
            totalWt = 0
            for weight in weights:
                totalWt+=weight
                if totalWt>mid:
                    daysNeeded+=1
                    totalWt=weight
            return daysNeeded<=days
        while l<=r:
            mid = (l+r)//2
            canBeShipped = isMinWeightCap(mid)
            if canBeShipped:
                ans = mid
                r=mid-1
            else:
                l=mid+1
        return ans