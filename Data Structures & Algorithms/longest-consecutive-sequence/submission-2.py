class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_lcs = 0
        num_set = set(nums)

        while(num_set):
            lcs = 1
            n = num_set.pop()
            r = n + 1
            l = n - 1
            while(r in num_set):
                num_set.remove(r)
                lcs += 1
                r += 1
            while(l in num_set):
                num_set.remove(l)
                lcs += 1
                l -= 1
            if lcs > max_lcs:
                max_lcs = lcs
        return max_lcs