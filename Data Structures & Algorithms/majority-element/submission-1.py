class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = defaultdict(int)
        for i in nums:
            mapping[i] = mapping[i]+1
            if mapping[i]>=len(nums)/2:
                return i
