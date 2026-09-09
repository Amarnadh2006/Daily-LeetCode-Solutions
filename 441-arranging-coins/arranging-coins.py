class Solution:
    def arrangeCoins(self, n: int) -> int:
        for x in range(n):
            a = ((x+1)*(x+2))/2
            if a > n:
                return x
            if a == n:
                return x+1
        