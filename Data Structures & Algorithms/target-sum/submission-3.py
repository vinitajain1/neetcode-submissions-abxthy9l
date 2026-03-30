class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(idx,amt):
            if (idx,amt) in dp:
                return dp[(idx,amt)]
            if idx>=len(nums):
                return 1 if amt==target else 0
            dp[(idx,amt)] = dfs(idx+1,amt+nums[idx])+dfs(idx+1,amt-nums[idx])
            return dp[(idx,amt)]
        return dfs(0,0)