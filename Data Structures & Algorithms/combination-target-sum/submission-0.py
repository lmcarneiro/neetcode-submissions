class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        s = []
        def dfs(i):
            if sum(s) == target:
                res.append(s.copy())
                return
            if i >= len(nums) or sum(s) > target:
                return
            
            s.append(nums[i])
            dfs(i)
            s.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

            