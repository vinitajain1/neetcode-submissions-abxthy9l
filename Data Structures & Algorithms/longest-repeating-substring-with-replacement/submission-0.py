class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count_map = defaultdict(int)
        l,r=0,0
        max_freq_char = 0
        for r in range(len(s)):
            count_map[s[r]]+=1
            window = r-l+1
            max_freq_char = max(max_freq_char,count_map.get(s[r],0))
            if(window-max_freq_char<=k):
                res = max(res,window)
            else:
                count_map[s[l]] -= 1
                l=l+1
        return res
        


            


        