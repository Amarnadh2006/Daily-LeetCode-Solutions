class Solution:
    def reverseDegree(self, s: str) -> int:
        c=0
        for x in range(len(s)):
            a=(x+1)*(123-ord(s[x]))
            c+=a
        return c
        