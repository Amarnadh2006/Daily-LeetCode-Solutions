class Solution:
    def average(self, salary: list[int]) -> float:
        big = max(salary)
        salary.remove(big)
        small = min(salary)
        salary.remove(small)
        total = sum(salary)/len(salary)
        return round(total,5)
        