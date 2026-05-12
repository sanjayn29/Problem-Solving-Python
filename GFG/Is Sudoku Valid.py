class Solution:
    def isValid(self, mat):
        # code here
        occured = set()
        for i in range(9):
            for j in range(9):
                num = mat[i][j]
                if num!=0:
                    rowkey=(num ,"row",i)
                    colkey=(num ,"col",j)
                    boxkey=(num,"box",i//3,j//3)
                    if rowkey in occured or colkey in occured or boxkey in occured:
                        return False
                    
                    occured.add(rowkey)
                    occured.add(colkey)
                    occured.add(boxkey)
        return True