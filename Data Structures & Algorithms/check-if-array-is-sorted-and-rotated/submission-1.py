class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        decrease = False
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                if decrease:
                    return False
                decrease = True
        return True
            