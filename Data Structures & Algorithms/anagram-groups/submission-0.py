class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        hashmap = {}
        for s in strs:
            freq_table = [0] * 26
            for l in s:
                ft_index = ord(l) - ord('a') # mapping lowercase letter to 0-25
                freq_table[ft_index] += 1
            if tuple(freq_table) in hashmap:
                hashmap[tuple(freq_table)].append(s)
            else:
                hashmap[tuple(freq_table)] = [s]
        
        
        ans = []
        for k in hashmap:
            ans.append(hashmap[k])
        return ans
