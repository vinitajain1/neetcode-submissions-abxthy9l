class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum%2:
            return False
        target = totalSum/2

        def dfs(i,target):
            if i>=len(nums):
                return target==0
            if target < 0:
                return False
            
            return dfs(i+1,target) or dfs(i+1,target-nums[i])
            
        return dfs(0,target)
