class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [[-1]*(len(nums)) for _ in range(len(nums))]
        def dfs(index,prev):
            if index>=len(nums):
                return 0
            if dp[index][prev]!=-1:
                return dp[index][prev]
            lis = dfs(index+1,prev)

            if prev==-1 or nums[prev]<nums[index]:
                lis = max(lis,1+dfs(index+1,index))
            dp[index][prev] = lis
            return lis
        
        return dfs(0,-1)