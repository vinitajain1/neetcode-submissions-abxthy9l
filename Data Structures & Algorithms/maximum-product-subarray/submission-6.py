class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = 1
        maxProd = 1
        res = max(nums)
        for i in range(len(nums)):
            currProd = maxProd * nums[i]
            maxProd = max(currProd,nums[i]*minProd,nums[i])
            minProd = min(currProd,nums[i]*minProd,nums[i])
            res = max(res,maxProd)
        return res