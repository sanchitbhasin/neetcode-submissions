class Solution:
    # lets try in O(log n) time
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_index = -1

        while left <= right:
            mid = (left + right) // 2
            if self.is_feasible(mid, nums):
                min_index = mid
                right = mid -1
            else:
                left = mid + 1
        return nums[min_index]


    def is_feasible(self, mid: int, nums: List[int]) -> bool:
        if nums[mid] <= nums[-1]:
            return True
        return False
