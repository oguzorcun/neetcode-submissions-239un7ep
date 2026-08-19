class Solution:
    def isHappy(self, n: int) -> bool:
        sumD = n
        sums = { sumD }

        while sumD != 1:
            sumD = self.sumDigits(sumD)
            if sumD in sums: return False
            sums.add(sumD)

        return True
        
    def sumDigits(self, n: int) -> int:
        sumD = 0
        while n > 0:
            sumD += (n % 10) ** 2
            n = n // 10
        return sumD