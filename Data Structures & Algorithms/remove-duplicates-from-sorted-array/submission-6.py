class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        rm_array = []
        for i in range(1, length):
            if nums[i - 1] == nums[i]:
                rm_array.append(i)

        for j, i in enumerate(rm_array):
            new_i = i - j
            nums[new_i:] = nums[new_i + 1:] + [nums[new_i]]
            
        return length - len(rm_array)
            