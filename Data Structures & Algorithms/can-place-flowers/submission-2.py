class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, filled in enumerate(flowerbed):
            if i == 0 and not filled:
                if len(flowerbed) > 1 and not flowerbed[i + 1]:
                    n -= 1
                    flowerbed[i] = 1
                elif len(flowerbed) == 1:
                    n -= 1
                    flowerbed[i] = 1
            
            elif i == len(flowerbed) - 1 and not filled and not flowerbed[i - 1]:
                n -= 1
                flowerbed[i] = 1

            elif i < len(flowerbed) - 1 and not filled and not flowerbed[i + 1] and not flowerbed[i - 1]:
                n -= 1
                flowerbed[i] = 1

            if n <= 0:
                return True
            
        return n <= 0
        

