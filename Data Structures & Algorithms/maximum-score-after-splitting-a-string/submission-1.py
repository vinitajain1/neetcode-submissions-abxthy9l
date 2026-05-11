class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = s.count('1')
        score = 0
        for i in range(len(s)-1):
            ch = s[i]
            if ch=='0':
                zeros+=1
            else:
                ones-=1
            score = max(score,zeros+ones)
        return score