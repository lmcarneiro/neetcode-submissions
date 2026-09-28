class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = 1
        k = 2
        res = set()
        nums.sort()

        while i < len(nums):
            while j < len(nums):
                while k < len(nums):
                    print(f"i: {i}, j: {j}, k: {k}")
                    if nums[i] + nums[j] + nums[k] == 0:
                        t = tuple([nums[i], nums[j], nums[k]])
                        print(t)
                        res.add(t)
                    k += 1
                j += 1
                k = j + 1
            i += 1
            j = i + 1
            k = j + 1
            print(f"i,j,k: {i}, {j}, {k}")
        print(res)
        print([list(i) for i in res])
        return list(res)
                