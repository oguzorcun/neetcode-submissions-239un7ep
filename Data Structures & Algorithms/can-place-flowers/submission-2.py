class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if 1 not in f[i-1:i+2]:
                f[i] = 1
                n -= 1
            if n <= 0: return True

        return False