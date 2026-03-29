class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        res = []
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxLen<r-l+1:
                    maxLen = r-l+1
                    res = [l,r]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxLen<r-l+1:
                    maxLen = r-l+1
                    res = [l,r]
                l-=1
                r+=1
        left,right = res
        return s[left:right+1]