class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1     
        chars = set()
        l,r = 0,1
        maxLen = 0   
        chars.add(s[l])
        while r<len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l=l+1
            chars.add(s[r])
            maxLen = max(maxLen,r-l+1)
            r=r+1
        return maxLen