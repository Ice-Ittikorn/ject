def checkmate(board):
    def check_Square():
        lines_board = board.count('\n') +1   # หาจำนวนบรรทัด
        line1 = board.split('\n')  # แยกบรรทัด
        naltang = len(line1[0])  # หาความยาว line 1
        if naltang != lines_board:
            print("Error : The table is not square")
        else:
            pass

    def check_lo() :
        lo_count = {'Q': 0, 'P': 0, 'R': 0,'K':0}
        for char_check in board:
            if char_check in {'Q', 'P','R','K'}:
                lo_count[char_check] += 1 
            elif char_check in {'.','\n'} :
                pass
            else :
                print(f"Error : There are others besides K Q P R")
        if lo_count['K'] == 0:
            print("Eror : Not is King")

        for key, value in lo_count.items():
            if value > 1:
                print(f"Error: {key} > 1")

    def is_king_in_check():
    # หาตำแหน่งของราชา (K)
        board_list = []
            for row in board.split('\n'):
                if row:
                    board_list.append(list(row))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    print(king_pos)
                    break

    check_Square()
    check_lo()
    is_king_in_check()

   


