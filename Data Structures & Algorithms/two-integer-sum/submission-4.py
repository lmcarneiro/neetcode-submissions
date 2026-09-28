class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1

        while i < len(nums):
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
            j = i + 1