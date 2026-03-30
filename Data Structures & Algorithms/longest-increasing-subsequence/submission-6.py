class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [10,9,2,5,3,7,101,18]
        lis = [1]*len(nums)
        res = lis[0]
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    lis[i] = max(lis[i],lis[j]+1)
            res = max(res,lis[i])
        return res 