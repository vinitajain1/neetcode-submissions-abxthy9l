class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(house):
            if house in dp:
                return dp[house]
            if house>=len(nums):
                return 0
            dp[house] = max(dfs(house+2)+nums[house],dfs(house+1))
            return dp[house]

        return dfs(0)