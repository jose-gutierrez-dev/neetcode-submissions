class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zp = 0
        tp = length - 1
        i = 0
        

        while(i <= tp):
            if nums[i] == 0:
                nums[i] = nums[zp]
                nums[zp] = 0
                zp += 1
            elif nums[i] == 2:
                nums[i] = nums[tp]
                nums[tp] = 2
                tp -= 1    
                continue
            i += 1
