class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r=0
        if len(t)==0:
            return ""
        countT = Counter(t)
        have=0
        need=len(countT)
        window=defaultdict(int)
        res = [-1,-1]
        resLen=float("inf")
        while r<len(s):
            ch = s[r]
            window[ch]+=1
            if ch in countT and window[ch]==countT[ch]:
                have+=1
            while have==need:
                if r-l+1<resLen:
                    res = [l,r]
                    resLen=r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
            r+=1
        l,r=res
        return s[l:r+1] if resLen!=float('inf') else ""

                