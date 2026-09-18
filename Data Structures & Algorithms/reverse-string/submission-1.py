class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        half_len = len(s) // 2
        r = len(s) - 1
        for i in range(0, half_len):
            char = s[i]
            s[i] = s[r]
            s[r] = char
            r -= 1
    