class Solution:
    # Time: O(N*M*3^L) where N*M is the number of elements in the board and L is the lenght of the word
    # Space: O(L) where L is the lenght of the word
    def exist(self, board: List[List[str]], word: str) -> bool:
        down, left = -1, -1
        up, right = 1, 1

        def backtrack(y, x, charIdx):
            if charIdx == len(word):
                return True
            if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]):
                return False
            if board[y][x] == '#':
                return False

            if board[y][x] == word[charIdx]:
                ch = board[y][x]
                board[y][x] = '#'
                found = (
                    backtrack(y + down, x, charIdx+1) or 
                    backtrack(y + up, x, charIdx+1) or
                    backtrack(y, x + left, charIdx+1) or
                    backtrack(y, x + right, charIdx+1) 
                )
                board[y][x] = ch
                return found

            return False

        for y in range(len(board)):
            for x in range(len(board[y])):
                found = backtrack(y, x, 0)
                if found:
                    return found
        
        return False

