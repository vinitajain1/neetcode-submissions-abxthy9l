class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        if len(nums)==1:
            return nums[0]
        def dfs(i,flag):
            if (i,flag) in dp:
                return dp[(i,flag)]
            if i>=len(nums) or (flag and i==len(nums)-1):
                return 0
            dp[(i,flag)] = max(nums[i]+dfs(i+2,flag),dfs(i+1,flag))
            return dp[(i,flag)]
        return max(dfs(0,True),dfs(1,False))