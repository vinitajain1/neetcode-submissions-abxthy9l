class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen=0
        l,r=0,0
        window = defaultdict(int)
        maxFreq=0
        while r<len(s):
            ch = s[r]
            window[ch]+=1
            maxFreq=max(maxFreq,window[ch])
            while (r-l+1)-maxFreq>k:
                window[s[l]]-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
            r+=1
        return maxLen