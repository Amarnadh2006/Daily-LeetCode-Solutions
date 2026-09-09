class Solution:
    def arrangeCoins(self, n: int) -> int:
        for x in range(n):
            if ((x+1)*(x+2))/2 > n:
                return x
            if ((x+1)*(x+2))/2 == n:
                return x+1
        