class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index_position = 0
        lcp = ""
        first_pass = True
        previous_letter = ""
        current_letter = ""
        while(True):
            for s in strs:
                if s == "":
                    return ""
                if len(s) == index_position:
                    return lcp
                current_letter = s[index_position]
                if first_pass:
                    previous_letter = current_letter
                    first_pass = False
                elif current_letter != previous_letter:
                    return lcp
            previous_letter = current_letter
            lcp += current_letter
            index_position += 1
            first_pass = True