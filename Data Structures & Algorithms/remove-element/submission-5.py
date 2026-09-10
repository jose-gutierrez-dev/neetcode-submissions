class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        i = 0
        length = len(nums)
        while(i != length):
            if nums[i] == val:
                del nums[i]
                length = len(nums)
            else:
                i += 1
        return length