class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = {}
        for i, n in enumerate(nums):
            if n in contains:
                return True
            contains[n] = i
        return False
        