class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        currArr = []
        def backtrack(i):
            res.append(currArr.copy())
            if i>=len(nums):
                return
            for j in range(i,len(nums)):
                currArr.append(nums[j])
                backtrack(j+1)
                currArr.pop()
        backtrack(0)
        return res
            