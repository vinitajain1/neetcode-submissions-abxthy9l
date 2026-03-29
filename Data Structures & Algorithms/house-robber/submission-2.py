class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def robbed(house):
            if house>=len(nums):
                return 0
            if dp[house]!=-1:
                return dp[house]
            dp[house] = max(nums[house] + robbed(house+2),robbed(house+1))
            return dp[house]
        return max(robbed(0),robbed(1))