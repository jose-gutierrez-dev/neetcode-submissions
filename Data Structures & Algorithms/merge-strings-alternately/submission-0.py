class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_words = ""
        op = 0
        tp = 0
        len_1 = len(word1)
        len_2 = len(word2)
        while op < len_1 or tp < len_2:
            if op < len_1:
                merged_words += word1[op]
                op += 1
            if tp < len_2:
                merged_words += word2[tp]
                tp += 1
        return merged_words