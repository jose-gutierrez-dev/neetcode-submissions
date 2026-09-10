import numpy as np
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        

        arr1 = np.array(nums)
  

# Optimal for 1D or general multi-dimensional arrays
        return list(np.concatenate((arr1, arr1)))  # or np.concat((arr1, arr2))