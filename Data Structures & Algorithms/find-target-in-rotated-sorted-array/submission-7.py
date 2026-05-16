# solution 2 - Binary search - treat nums as 2 arrays
# 1. find pivot point - that breaks nums into 2 sorted arrays
# 2. then finding a number in a sorted array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.find_pivot_index(nums)

        if target <= nums[-1] and target >= nums[min_index]:
            return self.binary_search(nums, min_index, len(nums)-1, target)
        else:
            return self.binary_search(nums, 0, min_index - 1, target)
    
    def find_pivot_index(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return l

    def binary_search(self, nums: List[int], start: int, end: int, target: int) -> int:
        l, r = start, end
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
            
