class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxProd = 1
        minProd = 1
        for i in nums:
            tmp = i*maxProd
            maxProd = max(i*maxProd,i*minProd,i)
            minProd = min(tmp,i*minProd,i)
            res = max(maxProd,res)
        return res