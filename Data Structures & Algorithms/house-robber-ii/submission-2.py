class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp = [[-1] * 2 for _ in range(len(nums))]
        def robbed(house,flag):
            if house>=len(nums) or (flag and house==len(nums)-1):
                return 0
            if dp[house][flag]!=-1:
                return dp[house][flag]
            dp[house][flag] = max(nums[house]+robbed(house+2,flag),robbed(house+1,flag))
            return dp[house][flag]
        return max(robbed(0,True),robbed(1,False))