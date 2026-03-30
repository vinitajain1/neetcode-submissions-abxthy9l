class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(idx,amt):
            if idx>=len(nums):
                return 1 if amt==target else 0
            return dfs(idx+1,amt+nums[idx])+dfs(idx+1,amt-nums[idx])
        return dfs(0,0)