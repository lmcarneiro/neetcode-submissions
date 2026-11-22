class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        mx = "0"
        max_i = 0
        swap_i, swap_j = -1, -1

        for i in reversed(range(len(arr))):
            if arr[i] > mx:
                mx = arr[i]
                max_i = i
            if arr[i] < mx:
                swap_i, swap_j = i, max_i

        arr[swap_i], arr[swap_j] = arr[swap_j], arr[swap_i]

        return int(''.join(arr))