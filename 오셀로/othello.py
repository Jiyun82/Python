#시작 화면: 모드 선택
#게임 화면: 컴모드 2인모드

import random

def start():
    while True:
        print("~~오셀로 게임~~")
        mode = int(input("1. 컴퓨터와 대결   2. 2인 모드\n선택: "))
        if mode == 1 or mode == 2:
            return mode

def print_board():
    print("  ", end = "")
    for i in range(0, 8):
        print(i, end = " ")
    print("")
    for r in range(8):
        print(r, end = " ")
        for c in range(8):
            if(board[r][c] == 0):
                print("O ", end = "")
            elif board[r][c] == 1:
                print("B ", end = "")
            elif board[r][c] == 2:
                print("W ", end = "")
            else:
                print("@ ", end = "")
        print("")

def check_leftup(r, c, color, other, fr, fc):
    if r - 1 >= 0 and c - 1 >= 0:
        if board[r - 1][c - 1] == other:
            check_leftup(r - 1, c - 1, color, other, fr, fc)
        elif board[r - 1][c - 1] == color:
            board[fr][fc] = 3
            global leftup
            leftup = 1
            #print("leftup: ", fr, fc)

def check_up(r, c, color, other, fr, fc):
    if r - 1 >= 0:
        if board[r - 1][c] == other:
            check_up(r - 1, c, color, other, fr, fc)
        elif board[r - 1][c] == color:
            board[fr][fc] = 3
            global up
            up = 1
            #print("up: ", fr, fc, r - 1, c)

def check_rightup(r, c, color, other, fr, fc):
    if r - 1 >= 0 and c + 1 <= 7:
        if board[r - 1][c + 1] == other:
            check_rightup(r - 1, c + 1, color, other, fr, fc)
        elif board[r - 1][c + 1] == color:
            board[fr][fc] = 3
            global rightup
            rightup = 1
            #print("rightup: ", fr, fc)

def check_left(r, c, color, other, fr, fc):
    if c - 1 >= 0:
        if board[r][c - 1] == other:
            check_left(r, c - 1, color, other, fr, fc)
        elif board[r][c - 1] == color:
            board[fr][fc] = 3
            global left
            left = 1
            #print("left: ", fr, fc)

def check_right(r, c, color, other, fr, fc):
    if c + 1 <= 7:
        if board[r][c + 1] == other:
            check_right(r, c + 1, color, other, fr, fc)
        elif board[r][c + 1] == color:
            board[fr][fc] = 3
            global right
            right = 1
            #print("right: ", fr, fc)

def check_leftdown(r, c, color, other, fr, fc):
    if r + 1 <= 7 and c - 1 >= 0:
        if board[r + 1][c - 1] == other:
            check_leftdown(r + 1, c - 1, color, other, fr, fc)
        elif board[r + 1][c - 1] == color:
            board[fr][fc] = 3
            global leftdown
            leftdown = 1
            #print("leftdown: ", fr, fc)

def check_down(r, c, color, other, fr, fc):
    if r + 1 <= 7:
        if board[r + 1][c] == other:
            check_down(r + 1, c, color, other, fr, fc)
        elif board[r + 1][c] == color:
            board[fr][fc] = 3
            global down
            down = 1
            #print("down: ", fr, fc)

def check_rightdown(r, c, color, other, fr, fc):
    if r + 1 <= 7 and c + 1 <= 7:
        if board[r + 1][c + 1] == other:
            check_rightdown(r + 1, c + 1, color, other, fr, fc)
        elif board[r + 1][c + 1] == color:
            board[fr][fc] = 3
            global rightdown
            rightdown = 1
            #print("rightdown: ", fr, fc)

def check_first(r, c, color, other):
    fr = r
    fc = c
    if(r == 0):
        if(c == 0):
            if(board[r][c + 1] == other):
                check_right(r, c + 1, color, other, fr, fc)
            if(board[r + 1][c] == other):
                check_down(r + 1, c, color, other, fr, fc)
            if(board[r + 1][c + 1] == other):
                check_rightdown(r + 1, c + 1, color, other, fr, fc)
        elif c == 7:
            if board[r][c - 1] == other:
                check_left(r, c - 1, color, other, fr, fc)
            if board[r + 1][c - 1] == other:
                check_leftdown(r + 1, c - 1, color, other, fr, fc)
            if board[r + 1][c] == other:
                check_down(r + 1, c, color, other, fr, fc)
        else:
            if(board[r][c - 1] == other):
                check_left(r, c - 1, color, other, fr, fc)
            if(board[r][c + 1]== other):
                check_right(r, c + 1, color, other, fr, fc)
            if(board[r + 1][c - 1] == other):
                check_leftdown(r + 1, c - 1, color, other, fr, fc)
            if(board[r + 1][c] == other):
                check_down(r + 1, c, color, other, fr, fc)
            if(board[r + 1][c + 1] == other):
                check_rightdown(r + 1, c + 1, color, other, fr, fc)
    
    elif r == 7:
        if c == 0:
            if board[r - 1][c] == other:
                check_up(r - 1, c, color, other, fr, fc)
            if board[r - 1][c + 1] == other:
                check_rightup(r - 1, c + 1, color, other, fr, fc)
            if board[r][c + 1] == other:
                check_right(r, c + 1, color, other, fr, fc)
        elif c == 7:
            if(board[r - 1][c - 1] == other):
                check_leftup(r - 1, c - 1, color, other, fr, fc)
            if board[r - 1][c] == other:
                check_up(r - 1, c, color, other, fr, fc)
            if board[r][c - 1] == other:
                check_left(r, c - 1, color, other, fr, fc)
        else:
            if(board[r - 1][c - 1] == other):
                check_leftup(r - 1, c - 1, color, other, fr, fc)
            if board[r - 1][c] == other:
                check_up(r - 1, c, color, other, fr, fc)
            if board[r - 1][c + 1] == other:
                check_rightup(r - 1, c + 1, color, other, fr, fc)
            if board[r][c - 1] == other:
                check_left(r, c - 1, color, other, fr, fc)
            if board[r][c + 1] == other:
                check_right(r, c + 1, color, other, fr, fc)
    
    elif c == 0:
        if board[r - 1][c] == other:
            check_up(r - 1, c, color, other, fr, fc)
        if board[r - 1][c + 1] == other:
            check_rightup(r - 1, c + 1, color, other, fr, fc)
        if board[r][c + 1] == other:
            check_right(r, c + 1, color, other, fr, fc)
        if board[r + 1][c] == other:
            check_down(r + 1, c, color, other, fr, fc)
        if board[r + 1][c + 1] == other:
            check_rightdown(r + 1, c + 1, color, other, fr, fc)
    
    elif c == 7:
        if(board[r - 1][c - 1] == other):
            check_leftup(r - 1, c - 1, color, other, fr, fc)
        if board[r - 1][c] == other:
            check_up(r - 1, c, color, other, fr, fc)
        if board[r][c - 1] == other:
            check_left(r, c - 1, color, other, fr, fc)
        if board[r + 1][c - 1] == other:
            check_leftdown(r + 1, c - 1, color, other, fr, fc)
        if board[r + 1][c] == other:
            check_down(r + 1, c, color, other, fr, fc)
        
    else:
        if(board[r - 1][c - 1] == other):#좌상
            check_leftup(r - 1, c - 1, color, other, fr, fc)
        if board[r - 1][c] == other:#상
            check_up(r - 1, c, color, other, fr, fc)
        if board[r - 1][c + 1] == other:#우상
            check_rightup(r - 1, c + 1, color, other, fr, fc)
        if board[r][c - 1] == other:#좌
            check_left(r, c - 1, color, other, fr, fc)
        if board[r][c + 1] == other:#우
            check_right(r, c + 1, color, other, fr, fc)
        if board[r + 1][c - 1] == other:#좌하
            check_leftdown(r + 1, c - 1, color, other, fr, fc)
        if board[r + 1][c] == other:#하
            check_down(r + 1, c, color, other, fr, fc)
        if board[r + 1][c + 1] == other:#우하
            check_rightdown(r + 1, c + 1, color, other, fr, fc)


def search_put(turn):
    if turn == "흑":
        color = 1
        other = 2
    else:
        color = 2
        other = 1
    
    for r in range(8):
        for c in range(8):
            if board[r][c] == 0:
                check_first(r, c, color, other)

def reverse(r, c):
    fr = r
    fc = c
    check_leftup(r - 1, c - 1, color, other, fr, fc)
    check_up(r - 1, c, color, other, fr, fc)
    check_rightup(r - 1, c + 1, color, other, fr, fc)
    check_left(r, c - 1, color, other, fr, fc)
    check_right(r, c + 1, color, other, fr, fc)
    check_leftdown(r + 1, c - 1, color, other, fr, fc)
    check_down(r + 1, c, color, other, fr, fc)
    check_rightdown(r + 1 , c + 1, color, other, fr, fc)

    board[r][c] = color
    if leftup:
        nr = r - 1
        nc = c - 1
        while board[nr][nc] == other:
            board[nr][nc] = color
            nr -= 1
            nc -= 1
    if up:
        nr = r - 1
        nc = c
        while board[nr][nc] == other:
            board[nr][nc] = color
            nr -= 1
    if rightup:
        nr = r - 1
        nc = c + 1
        while board[nr][nc] == other:
            board[nr][nc] = color
            nr -= 1
            nc += 1
    if left:
        nr = r
        nc = c - 1
        while board[nr][nc] == other:
            board[nr][nc] = color
            nc -= 1
    if right:
        nr = r
        nc = c + 1
        while board[nr][nc] == other:
            board[nr][nc] = color
            nc += 1
    if leftdown:
        nr = r + 1
        nc = c - 1
        while board[nr][nc] == other:
            board[nr][nc] = color
            nr += 1
            nc -= 1
    if down:
        nr = r + 1
        nc = c
        while board[nr][nc] == other:
            board[nr][nc] = color
            nr +=1
    if rightdown:
        nr = r + 1
        nc = c + 1
        while board[nr][nc] == other:
            board[nr][nc] = color
            nr += 1
            nc += 1

def clear_put():
    for r in range(8):
        for c in range(8):
            if board[r][c] == 3:
                board[r][c] = 0

def possibility():
    for r in range(8):
        for c in range(8):
            if board[r][c] == 3:
                return True
    return False

def full():
    for r in range(8):
        for c in range(8):
            if board[r][c] == 0 or board[r][c] == 3:
                return True
    return False

def count_score():
    black = 0
    white = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] == 1:
                black += 1
            elif board[r][c] == 2:
                white += 1
    if black > white:
        print("흑 승리")
    elif white > black:
        print("백 승리")
    else:
        print("비김")

def all_reversed():
    black = 0
    white = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] == 1:
                black +=1
            elif board[r][c] == 2:
                white += 1
    if black == 0:
        print("백 승리")
        return True
    elif white == 0:
        print("흑 승리")
        return True
    else:
        return False


board = [[0 for col in range(8)] for row in range(8)]
#0: 빈칸 1: 검정 2: 하양 3: 둘 수 있는 칸

mode = 0
turn = "흑"
color = 1
other = 2

leftup = 0
up = 0
rightup = 0
left = 0
right = 0
leftdown = 0
down = 0
rightdown = 0

board[3][3] = 2
board[3][4] = 1
board[4][3] = 1
board[4][4] = 2

mode = start()

while True:
    search_put(turn)

    v_possibility = possibility()

    fulled = full()
    v_all_reversed = all_reversed()

    print_board()

    if(fulled == False):
        print("종료")
        count_score()
        break

    if(v_all_reversed):
        print("종료")
        break

    print(turn)

    while True:
        if v_possibility == False:
            print("pass")
            if turn == "흑":
                turn = "백"
                color = 2
                other = 1
            else:
                turn = "흑"
                color = 1
                other = 2
            break

        if mode == 1 and turn == "백":
            can_put_list = []

            for r in range(8):
                for c in range(8):
                    if board[r][c] == 3:
                        can_put_list.append([r, c])
            
            com_choice = random.randint(0, len(can_put_list) - 1)

            row = can_put_list[com_choice][0]
            col = can_put_list[com_choice][1]
        else:
            row = int(input("행: "))
            col = int(input("열: "))

        if board[row][col] == 3:
            leftup = 0
            up = 0
            rightup = 0
            left = 0
            right = 0
            leftdown = 0
            down = 0
            rightdown = 0
            reverse(row, col)
            clear_put()

            if turn == "흑":
                turn = "백"
                color = 2
                other = 1
            else:
                turn = "흑"
                color = 1
                other = 2

            break
        else:
            print("다시 입력")