class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        right_side = [1] * len(nums) # we intilize all values to 1 because edge case of [-1] index
        left_side = [1] * len(nums) # we intilize all values to 1 because edge case of [0] index


        for i in range(len(nums) - 2, -1, -1):
            right_side[i] = right_side[i + 1] * nums[i + 1]

        res[0] = right_side[0]
        for i in range(1, len(nums)):
            left_side[i] = left_side[i - 1] * nums[i - 1]
            res[i] = left_side[i] * right_side[i]

        return res

        
        
        #for i in range(0, len(nums) - 1):
            #left_side[i + 1] = left_side[i] * nums[i + 1]
        # index at right side means 
        # I should be able to take same index to get multiples on either side of the number

    

        