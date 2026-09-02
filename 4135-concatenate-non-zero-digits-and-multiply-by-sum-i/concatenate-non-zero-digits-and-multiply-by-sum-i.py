class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        sum =0
        s = str(n)
        s = s.replace("0", "")
        for x in s:
            sum+=int(x)
        return int(s)*sum


        