class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
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