class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length_1 = len(nums)
        length_2 = len(set(nums))
        if length_1 == length_2:
            return False
        return True