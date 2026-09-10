class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zp = 0
        op = 0
        tp = 1
        for j in range(0, 2):
            for i, n in enumerate(nums):
                if n == j:
                    nums[i] = nums[zp]
                    nums[zp] = j
                    zp += 1

    

