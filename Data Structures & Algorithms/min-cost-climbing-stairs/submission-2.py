class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(index):
            if index in dp:
                return dp[index]
            if index>=len(cost):
                return 0
            dp[index] = min(dfs(index+1),dfs(index+2))+cost[index]
            return dp[index]

        return min(dfs(0),dfs(1))