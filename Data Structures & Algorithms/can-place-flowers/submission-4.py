class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
            
        arr = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) + 1):
            if sum(arr[i-1:i+2]) == 0:
                n -= 1
                arr[i] = 1

            if n == 0:
                return True
        
        return n <= 0