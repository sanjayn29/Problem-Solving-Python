class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        occ = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row = (num,"row",i)
                    col = (num,"col",j)
                    box = (num,"box",i//3,j//3)

                    if row in occ or col in occ or box in occ:
                        return False
                    
                    occ.add(row)
                    occ.add(col)
                    occ.add(box)
        return True
        