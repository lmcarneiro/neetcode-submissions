class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i = 0
        length = len(nums)
        removed = 0
        while i < length - 1:
            count += 1
            if nums[i - removed] == nums[i + 1 - removed]:
                if count >= 2:
                    val = nums.pop(i + 1 - removed)
                    nums.append(val)
                    removed += 1
            else:
                count = 0
            i += 1

        return length - removed