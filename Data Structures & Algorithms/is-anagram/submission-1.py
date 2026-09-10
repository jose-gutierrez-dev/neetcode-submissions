class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        each_letter = set(s)
        s_counter = 0
        t_counter = 0
        for l in each_letter:
            for letter in s:
                if l == letter:
                    s_counter += 1
            for letter in t:
                if l == letter:
                    t_counter += 1
            if s_counter != t_counter:
                return False
        return True