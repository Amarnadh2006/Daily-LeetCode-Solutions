class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        s = len(set(candyType))
        if s<(n//2):
            return s
        else:
            return n//2
        