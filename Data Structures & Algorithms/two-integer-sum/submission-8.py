class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        index_table = {}
        for i in range(0, length):
            current_num = nums[i]
            pair_needed = target - current_num
            if pair_needed in index_table:
                j = index_table[pair_needed]
                return [i, j] if i < j else [j, i]
            index_table[current_num] = i 


        """
        current_idx = 0
        while current_idx < length:
            for i in range(current_idx + 1, length):
                if nums[current_idx] + nums[i] == target:
                    return [current_idx, i]
            current_idx += 1
        """