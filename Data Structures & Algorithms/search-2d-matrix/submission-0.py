class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bot = len(matrix)-1

        while top<=bot:
            row = (top+bot)//2
            if matrix[row][-1] < target:
                top = row+1
            elif matrix[row][0]>target:
                bot = row - 1
            else:
                break
        
        if top<=bot:
            row = (top+bot)//2
        else:
            return False
        
        l = 0
        r = len(matrix[0])-1

        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid] > target:
                 r = mid-1
            elif matrix[row][mid]<target:
                l = mid+1
            else:
                return True
        return False
        