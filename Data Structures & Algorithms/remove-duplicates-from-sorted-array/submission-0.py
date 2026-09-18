class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        del_counter = 0
        length = len(nums)
        while r < length - del_counter:
            if nums[l] == nums[r]:
                del nums[r]
                del_counter += 1
                continue
            l += 1
            r += 1

        return length - del_counter
            