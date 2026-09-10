class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        front_i = 0
        back_i = 1
        length = len(nums)

        if nums == []:
            return 0
        if length == 1:
            if nums[0] == val:
                return 0
            else:
                return 1


        while(front_i + back_i < length):
            current_n = nums[front_i]
            if current_n != val:
                front_i += 1
            elif nums[-back_i] != val:
                nums[front_i] = nums[-back_i]
                nums[-back_i] = current_n
                back_i += 1
                front_i += 1
            else:
                back_i += 1
        if nums[front_i] == val:
            return front_i
        return front_i + 1
        '''
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
        '''