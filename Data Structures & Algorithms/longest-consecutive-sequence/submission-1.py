class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hash_set = set(nums)
        for num in nums:
            if num-1 not in nums:
                length=1
                while num+length in nums:
                    length = length+1
                longest = max(length,longest)
        return longest