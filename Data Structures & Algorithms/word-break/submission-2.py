class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {}
        def dfs(index):
            if index>=len(s):
                return True
            if index in dp:
                return dp[index]
            for j in range(index,len(s)):
                if s[index:j+1] in wordSet:
                    dp[index] = dfs(j+1)
                    if dp[index]==True:
                        return True
            return False

        return dfs(0)