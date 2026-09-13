class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            n = nums[i]
            if n != max:
                counter -= 1
                if counter == -1:
                    max = n
                    counter = 1
            else:
                counter += 1
        return max

