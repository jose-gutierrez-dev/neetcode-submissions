class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_lcs = 0
        link = set(nums)

        while(link):
            lcs = 1
            n = link.pop()
            r = n + 1
            l = n - 1
            while(r in link):
                link.remove(r)
                lcs += 1
                r += 1
            while(l in link):
                link.remove(l)
                lcs += 1
                l -= 1
            if lcs > max_lcs:
                max_lcs = lcs
        return max_lcs
                












"""
        link = set()
        for n in nums:
            link.add(n + 1)
            link.add(-(n - 1))


        while(link):
            n = link.pop()
            if n < 0:
                r = 
            lcs = 1
            r = n + 1
            l = -(n - 1)
            while(r in link):


        
        [2,3,0,5,4,6,1,1]

        #if n = -3 then num is 4... therefore we need to search for 3 or 5
        #if 3 is in set then 
"""