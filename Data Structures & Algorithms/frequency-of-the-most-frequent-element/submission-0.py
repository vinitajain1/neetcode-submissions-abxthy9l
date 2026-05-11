class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        res = 0
        runningSum = 0
        nums.sort()
        while r<len(nums):
            runningSum+=nums[r]
            while nums[r]*(r-l+1) > runningSum+k:
                runningSum-=nums[l]
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res
