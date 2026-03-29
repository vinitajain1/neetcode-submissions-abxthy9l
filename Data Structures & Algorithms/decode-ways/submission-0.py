class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        def dfs(pos):
            if pos in dp:
                return dp[pos]
            if pos>=len(s) or s[pos] == '0':
                return 0
            res = dfs(pos+1)
            if pos+1<len(s) and (s[pos] == "1" or (s[pos]=="2" and s[pos+1] in "0123456")):
                res = res + dfs(pos+2)
            dp[pos] = res
            return res


        return dfs(0)