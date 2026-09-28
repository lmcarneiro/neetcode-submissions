class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix * len(matrix[0])) - 1
        flat = [val for array in matrix for val in array]
        print(r)
        while l <= r:
            m = l + (r - l) // 2
            print(m)
            if flat[m] < target:
                l = m + 1
            elif flat[m] > target:
                r = m - 1
            else:
                return True
        return False
