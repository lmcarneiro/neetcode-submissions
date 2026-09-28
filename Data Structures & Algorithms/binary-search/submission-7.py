class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == target:
                return l
            else:
                l += 1
            if nums[r] == target:
                return r
            else:
                r -= 1
            
        return -1