class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=0,0
        s=""
        while l<len(word1) and r<len(word2):
            if(l==r):
                s=s+word1[l]
                l+=1
            else:
                s=s+word2[r]
                r+=1
        while l<len(word1):
            s=s+word1[l]
            l+=1
        while r<len(word2):
            s=s+word2[r]
            r+=1
        return s
        

