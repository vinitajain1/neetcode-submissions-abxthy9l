class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        knows = [0]*(n+1)
        if len(trust)<n-1:
            return -1
        for a,b in trust:
            knows[b]+=1
            knows[a]-=1
        print(knows)
        for person,k in enumerate(knows[1:],1):
            if k==n-1:
                return person
        return -1