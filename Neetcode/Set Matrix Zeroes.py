class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        fr = False
        fc = False

        for i in range(m):
            if matrix[i][0] == 0:
                fc = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                fr = True
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0

        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0

        if fr:
            for j in range(n):
                matrix[0][j] = 0

        if fc:
            for i in range(m):
                matrix[i][0] = 0       