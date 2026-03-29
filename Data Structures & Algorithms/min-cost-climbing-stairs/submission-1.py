class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        def climb(step):
            if step>=len(cost):
                return 0
            if dp[step]!=-1:
                return dp[step]
            dp[step] = cost[step]+min(climb(step+1),climb(step+2))
            return dp[step]
        return min(climb(0),climb(1))