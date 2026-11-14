class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        l = []
        n=-1
        for x in range(len(list1)):
            for y in range(len(list2)):
                if list1[x]==list2[y]:
                    if n==-1:
                        n=x+y
                        l.append(list1[x])
                    else:
                        if x+y <n:
                            n = x+y
                            l=[]
                            l.append(list1[x])
                        elif x+y == n:
                            l.append(list1[x])
        return l





        