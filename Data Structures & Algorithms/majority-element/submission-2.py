class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        max = 0
        res = 0
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
            if hashmap[n] > max:
                max = hashmap[n]
                res = n
        return res