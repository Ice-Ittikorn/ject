def checkmate(board):
    def check_Square():
        rows = board.strip().split('\n')
        num_rows = len(rows)
        square = True
        for row in rows:
            if len(row) != num_rows:
                square = False
        if square:
            return num_rows
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
        
    def Position_King():
        for y in range(len(board_list)):
            for x in range(len(board_list[y])):
                if board_list[y][x] == 'K':
                    king_pos = (x + 1, y + 1)
                    break   
        return king_pos      

    def Position_Pawn():
        pawn_positions = []
        for y in range(len(board_list)):
            for x in range(len(board_list[y])):
                if board_list[y][x] == 'P':
                    pawn_positions.append((x+1, y+1 ))
        return pawn_positions


    def Position_Bishop():
        bishop_positions = []
        for y in range(len(board_list)):
            for x in range(len(board_list[y])):
                if board_list[y][x] == 'B':
                    bishop_positions.append((x + 1, y + 1))
        print(f"Positions Bishop: {bishop_positions}")
        return bishop_positions

    def Position_Rook():
        rook_positions = []
        for y in range(len(board_list)):
            for x in range(len(board_list[y])):
                if board_list[y][x] == 'R':
                    rook_positions.append((x + 1, y + 1))
        return rook_positions
 
    def Position_Queen():
        queen_positions = []
        for y in range(len(board_list)):
            for x in range(len(board_list[y])):
                if board_list[y][x] == 'Q':
                    queen_positions.append((x + 1, y + 1))
        print(f"Positions Queen: {queen_positions}")
        return queen_positions

       

    def check():
        King_location = Position_King()
        def Pawn_check():
            pawn_positions = Position_Pawn()
            pawn_positions_check = []
            for position in pawn_positions:
                pawn_positions_check.append((position[0] - 1, position[1] - 1))
                pawn_positions_check.append((position[0] + 1, position[1] - 1))
            return pawn_positions_check

        def Bishop_check():
            pass

        def Rook_check():
            board_size = check_Square()
            Rook_positions = Position_Rook()
            Rook_position_check = []

            for position in Rook_positions:
                Rook_position_check = []
                x, y = position

                for posi in range(1, board_size + 1):
                    if posi != y:
                        Rook_position_check.append((x, posi))

                for posi in range(1, board_size + 1):
                    if posi != x:
                        Rook_position_check.append((posi, y))
            return Rook_position_check

        def Queen_check():
            pass

        Pawn_check()
        Bishop_check()
        Rook_check()
        Queen_check()

        King_posi = Position_King()
        Pawn_posi_check = Pawn_check()
        Rook_posi_check = Rook_check()

        print(f"King_posi : {King_posi}")
        print(f"Pawn_posi_check : {Pawn_posi_check}")
        print(f"Rook_posi_check : {Rook_posi_check}")


    
    check_Square()
    check_lo()
    # position ตาราง เป็นลิส 
    board_list = []
    for row in board.split('\n'):
        if row:
            board_list.append(list(row))

    Position_King()
    Position_Pawn()
    Position_Bishop()
    Position_Rook()
    Position_Queen()
    check()


   


