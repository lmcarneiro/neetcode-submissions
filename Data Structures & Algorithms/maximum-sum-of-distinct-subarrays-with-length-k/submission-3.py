class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        max_sum = 0
        window_sum = 0
        seen = set()
        for end, val in enumerate(nums):
            while val in seen:
                window_sum=window_sum-nums[start]
                seen.remove(nums[start])
                start+=1
            window_sum=window_sum+val
            seen.add(val)
            if end-start+1 == k:
                max_sum = max(max_sum, window_sum)
                window_sum=window_sum-nums[start]
                seen.remove(nums[start])
                start+=1
        return max_sum
