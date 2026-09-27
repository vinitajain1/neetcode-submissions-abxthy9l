class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l=1
        r=length-2
        # find peak
        while l<=r:
            m=(l+r)//2
            left,mid,right=mountainArr.get(m-1),mountainArr.get(m),mountainArr.get(m+1)
            if left<mid<right:
                l=m+1
            elif left>mid>right:
                r=m-1
            else:
                break
        l=0
        r=m-1
        while l<=r:
            pos=(l+r)//2
            mid=mountainArr.get(pos)
            if mid==target:
                return pos
            elif mid>target:
                r=pos-1
            else:
                l=pos+1
        l=m
        r=length-1
        while l<=r:
            pos=(l+r)//2
            mid=mountainArr.get(pos)
            if mid==target:
                return pos
            elif mid>target:
                l=pos+1
            else:
                r=pos-1
        return -1