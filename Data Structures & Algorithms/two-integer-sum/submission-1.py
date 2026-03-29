class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,val in enumerate(nums):
            val2 = target-val
            if val2 in hashMap:
                return [min(i,hashMap[val2]),max(i,hashMap[val2])]
            hashMap[val] = i
        return []