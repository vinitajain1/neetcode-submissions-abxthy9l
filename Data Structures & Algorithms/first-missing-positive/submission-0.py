class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        for i in range(len(nums)):
            if i+1 in hash_set:
                continue
            else:
                return i+1
        return len(nums)+1
        