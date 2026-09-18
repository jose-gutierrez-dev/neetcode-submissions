class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        l_stor, r_stor = None, None
        skipped = 0
        while l < r:
            if s[l] != s[r]:
                skipped += 1
                if skipped == 2:
                    break
                l_stor = l
                r_stor = r
                r += 1
            l += 1
            r -= 1

        if skipped != 2:
            return True

        l, r = l_stor, r_stor - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

        
        