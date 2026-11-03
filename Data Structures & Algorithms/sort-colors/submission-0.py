class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3

        for num in nums:
            buckets[num] += 1
            
        j = 0
        for i in range(3):
            for _ in range(buckets[i]):
                nums[j] = i
                j += 1
