class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        hashmap = {}
        for s in strs:
            freq_table = [0] * 26
            for l in s:
                ft_index = ord(l) - ord('a') # mapping lowercase letter to 0-25
                freq_table[ft_index] += 1
            tuple_key = tuple(freq_table)
            if tuple_key in hashmap:
                hashmap[tuple_key].append(s)
            else:
                hashmap[tuple_key] = [s]
        
        
        ans = []
        for k in hashmap:
            ans.append(hashmap[k])
        return ans
