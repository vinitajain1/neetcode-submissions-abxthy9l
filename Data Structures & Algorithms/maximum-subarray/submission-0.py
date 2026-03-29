class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        for i in nums:
            currSum = max(i+currSum,i)
            maxSum = max(currSum,maxSum)
        return maxSum