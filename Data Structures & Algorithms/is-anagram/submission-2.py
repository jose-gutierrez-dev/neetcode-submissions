class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict: {str, int} = {}
        t_dict: {str, int} = {}
        for i in range(0, len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        if s_dict == t_dict:
            return True
        return False
        """
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
        """