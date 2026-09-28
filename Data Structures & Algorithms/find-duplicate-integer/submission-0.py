class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            
            if nums[l] == nums[r]:
                return nums[l]
            
            prev_l = nums[l]
            prev_r = nums[r]
            l += 1
            r -= 1
                
            print(f"numL {nums[l]}, prevL {prev_l}, numR {nums[r]}, prevR {prev_r}")
            if nums[l] == prev_l or nums[r] == prev_l:
                return prev_l
            if nums[l] == prev_r or nums[r] == prev_r:
                return prev_r
        return nums[l]