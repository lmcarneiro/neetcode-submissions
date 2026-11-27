class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort()

        for i in range(l):
            if i != nums[i]:
                return i
        return l