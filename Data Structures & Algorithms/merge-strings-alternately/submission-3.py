class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_words = ""
        op = 0
        tp = 0
        len_1 = len(word1)
        len_2 = len(word2)
        while True:
            if op < len_1:
                merged_words += word1[op]
                op += 1
            else:
                return merged_words + word2[tp:]
            if tp < len_2:
                merged_words += word2[tp]
                tp += 1
            else:
                return merged_words + word1[op:]
        return merged_words