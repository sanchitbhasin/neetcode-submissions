class Solution:
    # lets try in O(n) time first
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
           ans = min(ans, nums[i])

        return ans