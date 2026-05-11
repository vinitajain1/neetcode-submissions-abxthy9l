class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0
        seen_mod = {0:-1}
        for i,num in enumerate(nums):
            prefix_mod  = (prefix_mod+num)%k
            if prefix_mod in seen_mod:
                if i-seen_mod[prefix_mod]>1:
                    return True
            else:
                seen_mod[prefix_mod] = i
        return False