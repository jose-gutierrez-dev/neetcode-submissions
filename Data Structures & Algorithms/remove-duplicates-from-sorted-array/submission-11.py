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

        '''
        length = len(nums)
        mv_counter = 0
        i = 1
        while i < length - mv_counter:
            if nums[i - 1] == nums[i]:
                nums[i:] = nums[i + 1:] + [nums[i]]
                mv_counter += 1
                continue
            i += 1

        return length - mv_counter
        '''