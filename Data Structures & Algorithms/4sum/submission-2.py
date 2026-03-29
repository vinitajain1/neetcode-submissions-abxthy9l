class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        quad = []
        def ksum(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue;
                    quad.append(nums[i])
                    ksum(k-1,i+1,target-nums[i])
                    quad.pop()
            else:
                l=start
                r=len(nums)-1
                while(l<r):
                    diff = nums[l] + nums[r]
                    if diff>target:
                        r=r-1
                    elif diff<target:
                        l=l+1
                    else:
                        res.append(quad + [nums[l],nums[r]])
                        l=l+1
                        while l<r and nums[l]==nums[l-1]:
                            l=l+1
        ksum(4,0,target)
        return res
