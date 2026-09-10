class Solution:
    def isNotSorted(self, nums: List[int]) -> bool:
        for i in range(0, len(nums) - 1):
            left_num = nums[i]
            if left_num > nums[i + 1]:
                return True
        return False

    def sortArray(self, nums: List[int]) -> List[int]:
        while(self.isNotSorted(nums)):
            for i in range(0, len(nums) - 1):
                left_num = nums[i]
                if left_num > nums[i + 1]:
                    nums[i] = nums[i + 1]
                    nums[i + 1] = left_num
        return nums