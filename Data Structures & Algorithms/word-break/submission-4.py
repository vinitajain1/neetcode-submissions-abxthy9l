class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {}
        def dfs(idx):
            if idx in dp:
                return dp[idx]
            if idx>=len(s):
                return True
            for j in range(idx,len(s)):
                if s[idx:j+1] in wordSet:
                    dp[idx] = dfs(j+1)
                    if dp[idx]:
                        return True
            return False
        return dfs(0)