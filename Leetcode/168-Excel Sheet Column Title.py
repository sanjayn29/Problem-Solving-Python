class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber = columnNumber -1
            rem = columnNumber%26
            ans += chr(ord("A")+rem)
            columnNumber=columnNumber//26
        return ans[::-1]