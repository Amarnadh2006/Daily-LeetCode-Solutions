class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        n=0
        for y in range(1,len(timeSeries)):
            if timeSeries[y]-timeSeries[y-1]<duration:
                n+=timeSeries[y]-timeSeries[y-1]
            else:
                n+=duration
        return n+duration


        