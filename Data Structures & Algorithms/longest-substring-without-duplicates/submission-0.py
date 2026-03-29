class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l=0
        r=0
        max_len = 0
        while(r<len(s)):
            if s[r] in window:
                while(s[r] in window):
                    window.remove(s[l])
                    l=l+1
            window.add(s[r])
            max_len = max(max_len,len(window))
            r=r+1
        return max_len
        