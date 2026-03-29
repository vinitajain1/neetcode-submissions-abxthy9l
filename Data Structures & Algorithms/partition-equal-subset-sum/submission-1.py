class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum%2:
            return False
        target = totalSum//2
        dp = [[-1]*(target+1) for _ in range(len(nums))]
        def dfs(i,target):
            if i>=len(nums):
                return target==0
            if target < 0:
                return False
            if dp[i][target]!=-1:
                return dp[i][target]
            
            dp[i][target] = dfs(i+1,target) or dfs(i+1,target-nums[i])

            return dp[i][target]
            
        return dfs(0,target)
