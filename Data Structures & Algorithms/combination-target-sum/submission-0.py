class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(index,sum):
            if sum==target:
                res.append(subset.copy())
                return
            if sum>target:
                return
            for i in range(index,len(nums)):
                subset.append(nums[i])
                dfs(i,sum+nums[i])
                subset.pop()
        dfs(0,0)
        return res