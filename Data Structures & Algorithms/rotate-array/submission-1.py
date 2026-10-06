import copy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        yo = nums.copy()
        for i in range(len(nums)):
            n = yo[i]
            index = (i + k) % len(nums)
            nums[index] = n