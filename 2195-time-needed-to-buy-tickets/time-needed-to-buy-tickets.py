class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        c=0
        n = tickets[k]
        for x in range(len(tickets)):
            if x<=k:
                if tickets[x]<n:
                    c+=tickets[x]
                else:
                    c+=n
            else:
                if tickets[x]>=n:
                    c+=n-1
                else:
                    c+=tickets[x]
        return c



        