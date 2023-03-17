def turn_line_num(board, turn):
    if board[0][0] == turn:
        if (board[0][0] == board[0][1]) and (board[0][1] == board[0][2]):
            return 1
        if (board[0][0] == board[1][0]) and (board[1][0] == board[2][0]):
            return 1
        if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
            return 1
    if board[1][1] == turn:
        if (board[1][0] == board[1][1]) and (board[1][1] == board[1][2]):
            return 1
        if (board[0][1] == board[1][1]) and (board[1][1] == board[2][1]):
            return 1
        if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
            return 1
    if board[2][2] == turn:
        if (board[2][0] == board[2][1]) and (board[2][1] == board[2][2]):
            return 1
        if (board[0][2] == board[1][2]) and (board[1][2] == board[2][2]):
            return 1
    return 0

def solution(board):
    answer = 1
    
    OCount = board[0].count('O') + board[1].count('O') + board[2].count('O')
    XCount = board[0].count('X') + board[1].count('X') + board[2].count('X')
    OLine = turn_line_num(board, 'O')
    XLine = turn_line_num(board, 'X')
    
    print(OCount, XCount, OLine, XLine)

    if XCount > OCount:
        answer = 0
    elif (OCount - XCount) > 1:
        answer = 0
    elif (OCount - XCount) == 1:
        if XLine > 0:
            answer = 0
    else:
        if OLine > 0:
            answer = 0
    return answer