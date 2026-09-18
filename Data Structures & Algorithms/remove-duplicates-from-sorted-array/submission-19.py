class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        un_index = 1
        for i in range(1, len(nums)):
            prev_val = nums[i - 1]
            cur_val = nums[i]
            if prev_val != cur_val:
                nums[un_index] = cur_val 
                un_index += 1
        return un_index