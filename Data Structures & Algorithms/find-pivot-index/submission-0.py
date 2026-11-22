class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        res = 0
        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)
        
        for i in range(len(nums)):
            if i == 0:
                left = 0
            else:
                left = prefix[i - 1]

            if i == len(nums) - 1:
                right = 0
            else:
                right = prefix[-1] - prefix[i]

            if right == left:
                return i

        return -1