class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        res = 0
        running_sum = 0
        for num in nums:
            running_sum = running_sum + num
            pre = running_sum-k
            res = res + prefix.get(pre,0)
            prefix[running_sum] = 1 + prefix.get(running_sum,0)
        return res