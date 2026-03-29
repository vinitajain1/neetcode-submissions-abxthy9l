class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxLen = 0
        seen = set()
        while r<len(s):
            while s[r] in seen:
              seen.remove(s[l])
              l+=1
            maxLen = max(maxLen,r-l+1)
            seen.add(s[r])
            r+=1
        return maxLen  