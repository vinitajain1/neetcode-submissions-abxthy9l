class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l=0
        r=0
        prod = 1
        if k<=1:
            return 0
        while r<len(nums):
            prod = prod*nums[r]
            while prod>=k and l<len(nums):
                prod = prod//nums[l]
                l+=1
            res+=(r-l+1)
            r+=1
        return res