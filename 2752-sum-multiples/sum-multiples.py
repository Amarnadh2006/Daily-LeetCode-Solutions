class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum=0
        for y in range(n):
            x=y+1
            if x%3==0 or x%5==0 or x%7==0:
                 sum+=x
        return sum

        