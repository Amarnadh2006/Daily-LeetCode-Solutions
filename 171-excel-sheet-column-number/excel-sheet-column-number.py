class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = len(columnTitle)
        c=0
        for x in range(l):
            c+=(26**(l-1-x))*(ord(columnTitle[x])-64)
        return c
            


        