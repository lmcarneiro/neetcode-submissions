class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from math import prod
        output = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            output[i] = prod(nums[i+1:] + nums[:i])

        return output