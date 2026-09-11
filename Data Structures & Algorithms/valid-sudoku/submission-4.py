from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap: dict[str, list[tuple[int, int]]] = defaultdict(list)
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != ".":
                    hashmap[num].append((i, j))

        for num, indices in hashmap.items():
            if len(indices) > 9:
                return False
            row_set = set()
            col_set = set()
            square_set = set()
            prev_length = 0

            for coordinate in indices:
                i = coordinate[0]
                j = coordinate[1]
                row_set.add(i)
                col_set.add(j)
                square_set.add((i // 3, j // 3))

                if prev_length == len(row_set) or prev_length == len(col_set) or prev_length == len(square_set):
                    return False
                prev_length += 1
        return True



        
        
        '''
        row_hashmap = {}
        for row in board:
            for num in row:
                if num == "." 

                        modded_i = i % 3
                modded_j = j % 3
                if (modded_i + 1 % 3, modded_j + 1 % 3) in indices:
                    return False
                if (modded_i - 1 % 3, modded_j + 1 % 3) in indices:
                    return False
                if (modded_i + 1 % 3, modded_j - 1 % 3) in indices:
                    return False
                if (modded_i - 1 % 3, modded_j - 1 % 3) in indices:
                    return False
        '''
        