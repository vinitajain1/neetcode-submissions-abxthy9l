class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        if len(nums)==1:
            return nums[0]
        def dfs(house,isFirst):
            if (house,isFirst) in dp:
                return dp[(house,isFirst)]
            if isFirst and house>=len(nums)-1:
                return 0
            elif house>=len(nums):
                return 0
            dp[(house,isFirst)] = max(dfs(house+2,isFirst)+nums[house],dfs(house+1,isFirst))
            return dp[(house,isFirst)]
        return max(dfs(0,True),dfs(1,False))