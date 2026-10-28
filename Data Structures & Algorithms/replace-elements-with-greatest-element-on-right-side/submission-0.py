class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr) - 1:
            arr[i] = max(arr[i + 1:])
            i += 1
        arr[-1] = -1
        return arr