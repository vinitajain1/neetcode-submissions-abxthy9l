class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumSeen = defaultdict(int)
        sumSeen[0] = 1
        res = 0
        runningSum = 0
        for i,num in enumerate(nums):
            runningSum+=num
            res+=sumSeen[runningSum-k]
            sumSeen[runningSum]+=1
        return res
