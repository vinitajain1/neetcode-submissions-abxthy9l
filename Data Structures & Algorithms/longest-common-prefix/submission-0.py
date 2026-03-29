class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        lcp = strs[0];
        for s in strs:
            while not s.startswith(lcp):
                lcp = lcp[:-1]
        return lcp
        