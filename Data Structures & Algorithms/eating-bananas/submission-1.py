class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # my max eating amount can be max(piles) because even if I eat more than max(piles) still the time needed would be same
        # you cannot eat 0 banans so l should start from 1
        l = 1
        r = max(piles)
        res = r
        while l<=r:
            mid = (l+r)//2

            timeNeeded = 0
            for p in piles:
                timeNeeded+=math.ceil(p/mid)
            if timeNeeded<=h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
