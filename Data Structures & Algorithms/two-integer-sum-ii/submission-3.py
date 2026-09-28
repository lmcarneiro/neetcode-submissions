class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(numbers)):
            print(h)
            print(f"idx: {i}, val: {numbers[i]}")
            if numbers[i] in h:
                return [h[numbers[i]]+1, i+1]
            h[target - numbers[i]] = i