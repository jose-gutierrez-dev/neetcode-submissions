class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        num_of_cp = 0
        for c in word:
            for i in range(1, len(strs)):
                if len(strs[i]) <= num_of_cp:
                    return word[0:num_of_cp]
                if c != strs[i][num_of_cp]:
                    return word[0:num_of_cp]
            num_of_cp += 1
        return word