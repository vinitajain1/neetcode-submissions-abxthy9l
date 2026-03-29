class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        if len(nums)==1:
            return nums[0]

        while l<=r:
            if nums[l]>nums[r]:
                l+=1
            else:
                return nums[l]
        