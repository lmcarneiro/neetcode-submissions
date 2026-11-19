class Solution:
    def check(self, nums: List[int]) -> bool:
        decrease = False
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                if decrease:
                    return False
                decrease = True
        return True
            