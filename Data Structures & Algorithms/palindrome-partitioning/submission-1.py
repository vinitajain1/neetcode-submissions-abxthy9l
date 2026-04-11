class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        subset = []

        def dfs(i,j):
            if(j>=len(s)):
                if i==j:
                    res.append(subset.copy())
                return
            if isPali(i,j):
                subset.append(s[i:j+1])
                dfs(j+1,j+1)
                subset.pop()
            dfs(i,j+1)

        def isPali(l,r):
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l=l+1
                r=r-1
            return True
        
        dfs(0,0)

        return res