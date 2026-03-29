class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=0
        r=len(matrix)-1
        while l<r:
            for i in range(r-l):
                t = l
                b = r
                tmp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = tmp
            l+=1
            r-=1
