class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]>0):
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                diff = nums[i] + nums[r] + nums[l]
                if diff==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    r=r-1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif diff>0:
                    r=r-1
                else:
                    l=l+1
        return res
                
        