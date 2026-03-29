class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        prev = 1
        for i in range(len(nums)):
            prefix[i]=prev
            prev = prev*nums[i]
        suffix = 1
        print(prefix)
        res = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            res[i] = prefix[i] * suffix
            suffix = suffix*nums[i]
        return res
