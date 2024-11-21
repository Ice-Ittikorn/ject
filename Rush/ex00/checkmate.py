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
        lo_count = {'Q': 0, 'P': 0, 'R': 0,'B':0, 'K':0}
        for char_check in board:
            if char_check in {'Q', 'P','R','B','K'}:
                lo_count[char_check] += 1 
            elif char_check in {'.','\n'} :
                pass
            else :
                print(f"Error : There are others besides K Q B P R")
        if lo_count['K'] == 0:
            print("Eror : Not is King")
        if lo_count['K'] > 1:
            print("Eror : King > 1")

    def position():
        # position ตาราง เป็นลิส 
        board_list = []
        for row in board.split('\n'):
            if row:
                board_list.append(list(row))

        def Position_King():
            for y in range(len(board_list)):
                for x in range(len(board_list[y])):
                    if board_list[y][x] == 'K':
                        king_pos = (x + 1, y + 1)
                        print(f"position king : {king_pos}")
                        break         

        def Position_Pawn():
            pawn_positions = []
            for y in range(len(board_list)):
                for x in range(len(board_list[y])):
                    if board_list[y][x] == 'P':
                        pawn_positions.append((x + 1, y + 1))
            print(f"Positions Pawn: {pawn_positions}")

        def Position_Bishop():
            bishop_positions = []
            for y in range(len(board_list)):
                for x in range(len(board_list[y])):
                    if board_list[y][x] == 'B':
                        bishop_positions.append((x + 1, y + 1))
            print(f"Positions Bishop: {bishop_positions}")

        def Position_Rook():
            rook_positions = []
            for y in range(len(board_list)):
                for x in range(len(board_list[y])):
                    if board_list[y][x] == 'R':
                        rook_positions.append((x + 1, y + 1))
            print(f"Positions Rook: {rook_positions}")

        def Position_Queen():
            queen_positions = []
            for y in range(len(board_list)):
                for x in range(len(board_list[y])):
                    if board_list[y][x] == 'Q':
                        queen_positions.append((x + 1, y + 1))
            print(f"Positions Queen: {queen_positions}")

        Position_King()
        Position_Pawn()
        Position_Bishop()
        Position_Rook()
        Position_Queen()

    def check_location():
        def Pawn_check():
            possible_positions = []
            for position in pawn_positions:
                possible_positions.append((position[0] - 1, position[1] - 1))
                possible_positions.append((position[0] - 1, position[1] + 1))
            print(possible_positions)

        def Bishop_check():
            pass
        def Rook_check():
            pass
        def Queen_check():
            pass
        Pawn_check()
        Bishop_check()
        Rook_check()
        Queen_check()
    
    check_Square()
    check_lo()
    position()
    check_location()

   


