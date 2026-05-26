class Solution:
    def rotateMatrix(self, matrix):
        # code here
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

        matrix.reverse()