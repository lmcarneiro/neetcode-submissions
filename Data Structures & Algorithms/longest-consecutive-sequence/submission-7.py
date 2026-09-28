class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        max_count = 0
        count = 1
        nums = sorted(nums)
        i = 1
        print(nums)
        while i < len(nums):
            if nums[i] - nums[i-1] <= 1:
                print(f"increasing count at index {i}")
                if nums[i] != nums[i-1]:
                    count += 1
            else:
                max_count = max(max_count, count)
                count = 1
            i += 1
        max_count = max(max_count, count)
        return max_count
