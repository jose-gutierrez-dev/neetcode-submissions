class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            elif len(hashmap) < 2:
                hashmap[n] = 1
            else:
                k1, k2 = hashmap
                v1, v2 = hashmap[k1], hashmap[k2]
                hashmap[k1] = v1 - 1
                if v1 - 1 == 0:
                    del hashmap[k1]
                hashmap[k2] = v2 - 1
                if v2 - 1 == 0:
                    del hashmap[k2]
        res = []
        if len(hashmap) == 0:
            return res
        check_hashmap = hashmap
        if len(hashmap) == 1:
            k1, = hashmap
            check_hashmap[k1] = 0
        else:
            k1, k2 = hashmap
            check_hashmap[k1], check_hashmap[k2] = 0, 0
        for n in nums:
            if n in check_hashmap:
                check_hashmap[n] += 1
        for k, v in check_hashmap.items():
            if v > len(nums) // 3:
                res.append(k)
        return res
        

