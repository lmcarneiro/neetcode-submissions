class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            idx = abs(n)
            if nums[idx - 1] < 0:
                res.append(idx)
            nums[idx - 1] = -nums[idx - 1]
        return res
