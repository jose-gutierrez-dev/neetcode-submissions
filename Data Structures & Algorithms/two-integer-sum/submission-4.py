class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        current_idx = 0
        while current_idx < length:
            for i in range(current_idx + 1, length):
                if nums[current_idx] + nums[i] == target:
                    return [current_idx, i]
            current_idx += 1
  
        

"""
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
""" 
