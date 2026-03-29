class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sorted_set = sorted(set(nums))
        nums[:len(sorted_set)] = sorted_set 
        return len(sorted_set)
        
        