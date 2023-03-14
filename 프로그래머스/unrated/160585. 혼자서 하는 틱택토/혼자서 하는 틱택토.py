#turn으로 완성된 줄의 개수를 출력하는 함수
def turn_line_num(board, turn):
    line = 0
    if board[0][0] == turn:
        if (board[0][0] == board[0][1]) and (board[0][1] == board[0][2]):
            line += 1
        if (board[0][0] == board[1][0]) and (board[1][0] == board[2][0]):
            line += 1
    if board[1][1] == turn:
        if (board[1][0] == board[1][1]) and (board[1][1] == board[1][2]):
            line += 1
        if (board[0][1] == board[1][1]) and (board[1][1] == board[2][1]):
            line += 1
        if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
            line += 1
        if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
            line += 1
    if board[2][2] == turn:
        if (board[2][0] == board[2][1]) and (board[2][1] == board[2][2]):
            line += 1
        if (board[0][2] == board[1][2]) and (board[1][2] == board[2][2]):
            line += 1
    return line

def solution(board):
    answer = 1
    
    OCount = board[0].count('O') + board[1].count('O') + board[2].count('O')
    XCount = board[0].count('X') + board[1].count('X') + board[2].count('X')
    OLine = turn_line_num(board, 'O')
    XLine = turn_line_num(board, 'X')
    
    print(OCount, XCount, OLine, XLine)
    
    #O가 선공이기에 무조건 X의 수보다 크거나 같으므로 X가 더 많으면 0
    if XCount > OCount:
        answer = 0
    #O와 X의 차이가 1보다 크면 O가 한 턴을 더 진행한 것이므로 0
    elif (OCount - XCount) > 1:
        answer = 0
    #O가 한턴 더 진행된 상태라면
    elif (OCount - XCount) == 1:
        #X가 이미 한 줄 이상이 완성된 상태라면 O는 더 이상 진행하지 못하므로 0
        if XLine > 0:
            answer = 0
    #O와 X의 개수가 같다면
    else:
        #O나 X가 이미 한 줄 이상이 완성된 상태라면 X는 더 이상 진행하지 못하므로 X
        if OLine > 0:
            answer = 0
    return answer