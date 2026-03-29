class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n):
            output = 0
            while n:
                digit = n%10
                digit=digit**2
                output+=digit
                n=n//10
            return output

        seen = set()
        while n not in seen:
            seen.add(n)
            n = sumOfSquares(n)
            if n==1:
                return True
        return False
            