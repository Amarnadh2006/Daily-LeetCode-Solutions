class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a =[]
        ans =0
        for x in nums:
            count = 0
            if x in a:
                continue
            else:
                for y in nums:
                    if y == x:
                        count +=1
                ans+= (count*(count-1))/2
                a.append(x)
        return int(ans)



        