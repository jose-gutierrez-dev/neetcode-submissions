class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        """
        length_1 = len(nums)
        length_2 = len(set(nums))
        if length_1 == length_2:
            return False
        return True
        """