class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate((nums)): 
            a = target - nums[i]
            if a in seen:
                result = [seen[a], i]
                return result
            seen[j] = i