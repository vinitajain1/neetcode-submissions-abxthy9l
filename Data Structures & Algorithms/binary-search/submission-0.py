class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binarySearch(l,r):
            if l>r:
                return -1
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return binarySearch(mid+1,r)
            else:
                return binarySearch(l,mid-1)
            return -1

        l = 0
        r = len(nums)-1
        return binarySearch(l,r)