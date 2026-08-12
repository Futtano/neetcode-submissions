class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_buck = {
            i : set() for i in range(len(board))
        }
        col_buck = {
            j : set() for j in range(len(board[0]))
        }
        quadrant_buck = {
            (i, j) : set() for i in range (3) for j in range(3)
        }

        for i in range(len(board)):
            for j in range(len(board[0])):
                el = board[i][j]
                if el != '.':
                    # Check board validity
                    quad_i, quad_j = i // 3, j // 3
                    row_valid = not (el in row_buck[i])
                    col_valid = not (el in col_buck[j])
                    quad_valid = not (el in quadrant_buck[(quad_i, quad_j)])

                    # if any of this is False,
                    # the validity invariant has been broken
                    if not row_valid or not col_valid or not quad_valid:
                        return False
                    
                    # add element to each bucket
                    row_buck[i].add(el)
                    col_buck[j].add(el)
                    quadrant_buck[(quad_i, quad_j)].add(el)

        return True


