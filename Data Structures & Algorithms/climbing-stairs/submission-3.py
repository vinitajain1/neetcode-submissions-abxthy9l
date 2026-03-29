class Solution:
    def climbStairs(self, n: int) -> int:
        map = {}
        def climb(sum):
            if sum in map:
                return map[sum]
            if sum==n:
                return 1
            elif sum > n:
                return 0
            else:
                map[sum] = climb(sum+1) + climb(sum+2)
                return map[sum]
        return climb(1) + climb(2)