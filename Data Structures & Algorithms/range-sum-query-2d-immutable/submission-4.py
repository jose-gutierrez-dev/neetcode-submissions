class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.prefixes = [0] * (self.width * self.height)

        def matrix_val(i: int, j: int) -> int:
            return self.prefixes[i * self.width + j]

        k = 0
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):  
                if i == 0:                
                    self.prefixes[k] = self.prefixes[k - 1] + value
                elif j == 0:
                    self.prefixes[k] = matrix_val(i - 1, j) + value
                else:
                    upper_matrix = matrix_val(i - 1, j)
                    left_matrix = matrix_val(i, j - 1)
                    overlap_matrix = matrix_val(i - 1, j - 1)
                    self.prefixes[k] = upper_matrix + left_matrix - overlap_matrix + value
                k += 1
                    

#k = i * width + j

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def matrix_val(i: int, j: int) -> int:
            return self.prefixes[i * self.width + j]
        
        outer_matrix, left_matrix, upper_matrix, overlap_matrix = matrix_val(row2, col2), 0, 0, 0
        
        if col1 > 0 and row1 > 0:
            overlap_matrix = matrix_val(row1 - 1, col1 - 1)
            left_matrix = matrix_val(row2, col1 - 1)
            upper_matrix = matrix_val(row1 - 1, col2)
        elif col1 > 0: 
            left_matrix = matrix_val(row2, col1 - 1)
        elif row1 > 0:
            upper_matrix = matrix_val(row1 - 1, col2)

        return outer_matrix - left_matrix - upper_matrix + overlap_matrix

            



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)