class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)<=1:
            return len(s)
        hashMap = {}
        l,r = 0,0
        maxLen = 0
        maxFreq = 0
        while r<len(s):
            hashMap[s[r]] = 1+hashMap.get(s[r],0)
            maxFreq = max(maxFreq,hashMap[s[r]])
            while (r-l+1) - maxFreq >k:
                hashMap[s[l]]-=1
                l+=1
            maxLen = max(maxLen,r-l+1)
            r+=1
        return maxLen


        