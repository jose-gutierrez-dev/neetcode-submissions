class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [None] * length

        res[-1] = 1
        for i in range(length - 2, -1, -1):
            res[i] = res[i + 1] * nums[i + 1]

        prior_value = 1
        for i in range(1, length):
            prior_value = prior_value * nums[i - 1]
            res[i] = prior_value * res[i]

        return res