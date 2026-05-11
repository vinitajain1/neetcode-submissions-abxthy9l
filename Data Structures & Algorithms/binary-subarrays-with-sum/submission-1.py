class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        runningSum = 0
        seen = defaultdict(int)
        seen[0]=1
        for num in nums:
            runningSum+=num
            res+=seen[runningSum-goal]
            seen[runningSum]+=1
        return res