class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_val = None
        un_index = 0
        for cur_val in nums:
            if prev_val != cur_val:
                nums[un_index] = cur_val 
                un_index += 1
                prev_val = cur_val
        return un_index