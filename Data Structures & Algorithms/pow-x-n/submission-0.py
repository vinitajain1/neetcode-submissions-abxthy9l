class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        num = 1
        for i in range(abs(n)):
            num = num*x
        return num if n>=0 else 1/num