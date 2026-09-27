class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(leftBias):
            l=0
            r=len(nums)-1
            res = -1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    if leftBias:
                        res=mid
                        r=mid-1
                    else:
                        res=mid
                        l=mid+1
            return res
        left = binarySearch(True)
        right = binarySearch(False)
        return [left,right]
