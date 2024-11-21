def checkmate(board):
    def check_Square():
        rows = board.strip().split('\n')
        num_rows = len(rows)
        square = True
        for row in rows:
            if len(row) != num_rows:
                square = False
        if square:
            pass
        else:
            print("Eror : The board is not a square.")

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
        if lo_count['K'] > 1:
            print("Eror : King > 1")

    def position():
        #position ตาราง เป็นลิส 
        board_list = []
        for row in board.split('\n'):
            if row:
                board_list.append(list(row))

        def Position_King():
            for i in range(len(board_list)):
                for j in range(len(board_list[i])):
                    if board_list[i][j] == 'K':
                        king_pos = (i+1, j+1)
                        print(f"position king : {king_pos}")
                        break         
        def Position_Pawn():
            for i in range(len(board_list)):
                for j in range(len(board_list[i])):
                    if board_list[i][j] == 'P':
                        Pawn_pos = (i+1, j+1)
                        print(f"position Pawn : {Pawn_pos}")
                        break
        def Position_Bishop():
            for i in range(len(board_list)):
                for j in range(len(board_list[i])):
                    if board_list[i][j] == 'B':
                        Bishop_pos = (i+1, j+1)
                        print(f"position Pawn : {Bishop_pos}")
                        break
        def Position_Rook():
            for i in range(len(board_list)):
                for j in range(len(board_list[i])):
                    if board_list[i][j] == 'R':
                        Rook_pos = (i+1, j+1)
                        print(f"position Rook : {Rook_pos}")
                        break
        def Position_Queen():
            for i in range(len(board_list)):
                for j in range(len(board_list[i])):
                    if board_list[i][j] == 'Q':
                        Queen_pos = (i+1, j+1)
                        print(f"position Queen : {Queen_pos}")
                        break
        Position_King()
        Position_Pawn()
        Position_Bishop()
        Position_Rook()
        Position_Queen()

    check_Square()
    check_lo()
    position()

   


