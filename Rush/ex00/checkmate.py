def checkmate(board):
    def check_Square():
        check_error = True
        square = True
        rows = board.strip().split('\n')
        num_rows = len(rows)
        for row in rows:
            if len(row) != num_rows:
                square = False
        if square:
            check_error = True
        else:
            print("Error: The board is not a square.")
            check_error = False
        return check_error  
    
    def check_lo() :
        check_error = True
        lo_count = {'Q': 0, 'P': 0, 'R': 0,'B':0, 'K':0}
        for char_check in board:
            if char_check in {'Q', 'P','R','B','K'}:
                lo_count[char_check] += 1 
            elif char_check in {'.','\n'} :
                pass
            else :
                print(f"Error : There are others besides K Q B P R")
                check_error = False
                
        if lo_count['K'] == 0:
            print("Error : Not is King")
            check_error = False
            
        if lo_count['K'] > 1:
            print("Error : King > 1")
            check_error = False
        return check_error

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
            rows = board.strip().split('\n')
            board_size = len(rows)
            Bishop_positions = Position_Bishop()
            Bishop_position_check = []

            for position in Bishop_positions:
                x, y = position

                # ตรวจสอบการเดินในแนวทแยงมุมทั้ง 4 ทิศทาง
                for i in range(1, board_size + 1):
                    if x + i <= board_size and y + i <= board_size:
                        Bishop_position_check.append((x + i, y + i))
                    if x - i > 0 and y + i <= board_size:
                        Bishop_position_check.append((x - i, y + i))
                    if x + i <= board_size and y - i > 0:
                        Bishop_position_check.append((x + i, y - i))
                    if x - i > 0 and y - i > 0:
                        Bishop_position_check.append((x - i, y - i))

            return Bishop_position_check

        def Rook_check():
            rows = board.strip().split('\n')
            board_size = len(rows)
            Rook_positions = Position_Rook()
            Rook_position_check = []

            for position in Rook_positions:
                x, y = position

                for posi in range(1, board_size + 1):
                    if posi != y:
                        Rook_position_check.append((x, posi))

                for posi in range(1, board_size + 1):
                    if posi != x:
                        Rook_position_check.append((posi, y))
            return Rook_position_check

        def Queen_check():
            rows = board.strip().split('\n')
            board_size = len(rows)
            Queen_positions = Position_Queen()
            Queen_position_check = []
            for position in Queen_positions:
                x, y = position
                for i in range(1, board_size + 1):
                    if x + i <= board_size and y + i <= board_size:
                        Queen_position_check.append((x + i, y + i))
                    if x - i > 0 and y + i <= board_size:
                        Queen_position_check.append((x - i, y + i))
                    if x + i <= board_size and y - i > 0:
                        Queen_position_check.append((x + i, y - i))
                    if x - i > 0 and y - i > 0:
                        Queen_position_check.append((x - i, y - i))

            for position in Queen_positions:
                x, y = position
                for posi in range(1, board_size + 1):
                    if posi != y:
                        Queen_position_check.append((x, posi))
                for posi in range(1, board_size + 1):
                    if posi != x:
                        Queen_position_check.append((posi, y))

            return Queen_position_check

        King_posi = Position_King()
        Pawn_posi_check = Pawn_check()
        Bishop_posi_check = Bishop_check()
        Rook_posi_check = Rook_check()
        Queen_posi_check = Queen_check()

        list_in_check = Pawn_posi_check + Bishop_posi_check + Rook_posi_check + Queen_posi_check
        if King_posi in list_in_check :
            print ("Success")
        else:
            print("Fail")


    #run
    check_error = check_Square()
    check_error2 = check_lo()

    # position ตาราง เป็นลิส 
    board_list = []
    for row in board.split('\n'):
        if row:
            board_list.append(list(row))

    if check_error == True and check_error2 == True:
        Position_King()
        Position_Pawn()
        Position_Bishop()
        Position_Rook()
        Position_Queen()
        check()