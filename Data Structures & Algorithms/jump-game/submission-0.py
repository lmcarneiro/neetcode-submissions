class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = len(nums) - 1
        for i in range(n - 2, -1, -1):
            if nums[i] >=  goal - i:
                goal = i
        return goal == 0