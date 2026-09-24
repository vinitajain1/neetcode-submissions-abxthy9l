class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def getTotalBananas(eatingRate):
            totalHrs = 0
            for pile in piles:
                totalHrs+=math.ceil(pile/eatingRate)
            return totalHrs<=h
        while l<=r:
            mid = (l+r)//2
            totalBananas = getTotalBananas(mid)
            if totalBananas:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans