class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==0:
            return [[]]
        subset = []
        res = []
        def dfs():
            if len(subset)==len(nums):
                res.append(subset.copy())
            for i in range(len(nums)):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    dfs()
                    subset.pop()
        dfs()
        return res