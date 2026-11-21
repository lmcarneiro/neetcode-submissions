class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = []
        total = 0
        for n in nums:
            total += n
            self.pre_sum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.pre_sum[right]
        left_sum = self.pre_sum[left - 1] if left > 0 else 0
        return right_sum - left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)