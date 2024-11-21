def checkmate(board):
    def check_Square():
        lines_board = board.count('\n')   # หาจำนวนบรรทัด
        line1 = board.split('\n')  # แยกบรรทัด
        naltang = len(line1[0])  # หาความยาว line 1
        if naltang != lines_board:
            print("Error : talang mai pan jatturat")
        else:
            pass

    def check_King():
        count_K = board.count('K')
        if count_K > 1:
            print("King mak kar 1")
        elif count_K == 0:
            print("mai me King ")

    def check_lo() :
        for char in  {'K', 'Q', 'P', 'R'}:
            count = 0
            lo_count = []
            for char_check in board:
                if char_check in {'K', 'Q', 'P', 'R'}:
                    count += 1
                    lo_count[char_check] = count
                elif char_check in {'.','\n'} :
                    pass
                else :
                    print(f"Error : me tre aeen nog ja K Q P R")

            result = {
                key: value
                for key, value in lo_count.items()
                    if value > 1 :
                        print(f"Eror : me {key} mak kar 1")
                        result[key] = value
                    else :
                        print("nome")
            }

    check_Square()
    check_King()
    check_lo()

   


