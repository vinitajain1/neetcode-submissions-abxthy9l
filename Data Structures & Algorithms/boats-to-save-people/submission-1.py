class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l=0
        r=len(people)-1
        #[1,2,4,5]
        while l<=r:
            currWt = people[l]+people[r]
            boats+=1
            if currWt<=limit:
                l+=1
                r-=1
            elif currWt>limit:
                r-=1
        return boats
