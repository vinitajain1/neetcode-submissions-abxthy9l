class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        l=0
        r=len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                left = mid
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        right = -1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                right = mid
            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid-1
        return [left,right]
        
