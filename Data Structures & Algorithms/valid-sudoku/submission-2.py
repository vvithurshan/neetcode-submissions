class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows

        for row in board:
            rows = []

            for r in row:
                if r != ".":
                    rows.append(r)

            if len(rows) != len(set(rows)):
                return False


        # cols

        for row in range(9):
            cols = []

            for col in range(9):
                if board[col][row] != ".":
                    cols.append(board[col][row])

            if len(cols) != len(set(cols)):
                return False

        # quarter
        # 0: 3, 3:6, 6:9

        Q = [[] for i in range(9)]

        for row in range(9):
            for col in range(9):
                if row < 3:
                    if col < 3:
                        Q[0].append(board[row][col])
                    
                    elif col < 6:
                        Q[1].append(board[row][col])

                    elif col < 9:
                        Q[2].append(board[row][col])

                elif row < 6:
                    if col < 3:
                        Q[3].append(board[row][col])
                    
                    elif col < 6:
                        Q[4].append(board[row][col])

                    elif col < 9:
                        Q[5].append(board[row][col])

                elif row < 9:
                    if col < 3:
                        Q[6].append(board[row][col])
                    
                    elif col < 6:
                        Q[7].append(board[row][col])

                    elif col < 9:
                        Q[8].append(board[row][col])

                        
        # check each square

        for square in Q:

            setsquare = []

            for val in square:
                if val != ".":
                    setsquare.append(val)

            if len(setsquare) != len(set(setsquare)):
                return False

        return True








