class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contains = {}
        contains[nums[0]] = 0
        for i in range(1, len(nums)):
            value = target - nums[i]
            if value in contains:
                return [contains[value], i]
            
            # add current value to contains map
            contains[nums[i]] = i
        return Nill;
