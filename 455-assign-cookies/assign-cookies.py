class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i,j,c=0,0,0
        p = len(g)
        q = len(s)
        while (i!=p and j!=q):
            if g[i]<=s[j]:
                c+=1
                i+=1
                j+=1
            else:
                j+=1
        return c


        