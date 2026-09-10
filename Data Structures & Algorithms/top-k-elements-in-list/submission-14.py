class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        max_nums = []
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        length = len(nums)
        res_array = [[] for _ in range(length + 1)]
        for key, v in hashmap.items():
            res_array[v].append(key)

        res = []
        for i in range(len(res_array) - 1, -1, -1):
            if len(res) == k:
                    return res
            for n in res_array[i]:
                res.append(n)
            
                
            



        

        