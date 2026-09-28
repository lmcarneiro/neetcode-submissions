class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            m = l + (r - l) // 2
            print(m)
            print(m+1)

            if nums[r] == target:
                return r
            if nums[l] == target:
                return l

            if nums[m] > target:
                l += 1
            elif nums[m] < target:
                r -= 1
            else:
                return m
        return -1