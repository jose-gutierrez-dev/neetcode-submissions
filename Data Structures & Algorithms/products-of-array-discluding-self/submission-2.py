class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [None] * length
        right_side = [None] * length 
        left_side = [None] * length 

        right_side[-1] = 1
        for i in range(length - 2, -1, -1):
            right_side[i] = right_side[i + 1] * nums[i + 1]

        left_side[0] = 1
        res[0] = right_side[0]
        for i in range(1, length):
            left_side[i] = left_side[i - 1] * nums[i - 1]
            res[i] = left_side[i] * right_side[i]

        return res


        