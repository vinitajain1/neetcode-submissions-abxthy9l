class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        dl = 0
        while(l<r):
            if s[l]==s[r]:
                l+=1
                r-=1
                continue
            elif dl==0:
                if s[l]==s[r-1]:
                    r-=1
                else:
                    l+=1
                dl+=1
            else:
                return False;
        return True


        