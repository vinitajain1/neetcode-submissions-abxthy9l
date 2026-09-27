class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        res = 0
        def canSplitK(mid):
            split = 1
            currSum = 0
            for num in nums:
                currSum+=num
                if currSum>mid:
                    split+=1
                    currSum=num
            return split<=k
        while l<=r:
            mid = (l+r)//2
            canSplit = canSplitK(mid)
            if canSplit:
                res = mid
                r=mid-1
            else:
                l=mid+1
        return res
        