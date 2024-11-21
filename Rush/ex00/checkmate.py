def checkmate(board):
    def check_Square():
        lines_board = board.count('\n') + 1  # หาจำนวนบรรทัด
        line1 = board.split('\n')  # แยกบรรทัด
        naltang = len(line1[0])  # หาความยาว line 1

        if naltang != lines_board:
            print("Error : talang mai pan jatturat")

    def check_King():
        count_K = board.count('K')
        if count_K > 1:
            print("King mak kar 1")
        elif count_K == 0:
            print("mai me King ")

    def check_lo() :
        all_lo = {'.', 'K', 'Q', 'P', 'R' , '\n'}
        for char in board:
            if char not in all_lo:
                print("Error : me tre aeen nog ja K Q P R")

    check_Square()
    check_King()
    check_lo()

   

