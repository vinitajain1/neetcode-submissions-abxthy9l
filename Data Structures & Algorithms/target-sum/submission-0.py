class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def dfs(index,target):
            if index>=len(nums) and target==0:
                return 1
            if index>=len(nums):
                return 0
            ways = 0
            ways = ways + dfs(index+1,target-nums[index]) + dfs(index+1,target+nums[index])

            return ways

        return dfs(0,target)