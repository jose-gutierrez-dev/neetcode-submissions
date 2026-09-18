class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        un_index = 0
        for i in range(1, len(nums)):
            prev_val = nums[i - 1]
            cur_val = nums[i]
            if prev_val != cur_val:
                un_index += 1
                nums[un_index] = cur_val 
                prev_val = cur_val
        return un_index + 1