import pygame
import random

pygame.init()

#화면 세팅
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Othello")

#색깔
black = (0, 0, 0)
white = (255, 255, 255)
lavender = (200, 191, 231)

#보드 세팅
board = [[0 for col in range(8)] for row in range(8)]
#0: 빈칸 1: 검정 2: 하양 3: 둘 수 있는 칸

board[3][3] = 2
board[3][4] = 1
board[4][3] = 1
board[4][4] = 2

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

#메인코드
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

def search_put():
    global turn
    global color
    global other

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
        return 1
    elif white > black:
        print("백 승리")
        return 2
    else:
        print("비김")
        return 3
    #quitgame()

def auto():
    can_put_list = []

    for r in range(8):
        for c in range(8):
            if board[r][c] == 3:
                can_put_list.append([r, c])
    
    if len(can_put_list) > 0:
        com_choice = random.randint(0, len(can_put_list) - 1)

        row = can_put_list[com_choice][0]
        col = can_put_list[com_choice][1]

        puted(row, col)

#그래픽 메인 코드
def text_objects(text, font):#텍스트
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(txt, x, y, w, h, ic, ac, font, action=None):#버튼
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h> mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()        
    else: 
        pygame.draw.rect(screen, ic, (x, y, w, h))
    
    textSurt, textRect = text_objects(txt, font)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurt, textRect)

def quitgame():
    pygame.quit()
    #sys.exit()

def start():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        
        button("1p", screen_width * 0.5 - 150, screen_height * 0.1, 300, 100, 100, 100, pygame.font.SysFont(None, 50), onep)
        button("2p", screen_width * 0.5 - 150, screen_height * 0.8, 300, 100, 100, 100, pygame.font.SysFont(None, 50), twop)

        pygame.display.update()

def onep():
    game(1)
def twop():
    game(2)

def draw_board():
    for r in range(8):
        for c in range(8):
            rect_x = 170 + 70 * r
            rect_y = 20 + 70 * c
            rect_width = 70
            rect_height = 70
            pygame.draw.rect(screen, black, (rect_x, rect_y, rect_width, rect_height), 3)

def draw_stone():
    for r in range(8):
        for c in range(8):
            rad = 30
            circle_x = 170 + 70 * r + 35
            circle_y = 20 + 70 * c + 35
            if board[r][c] == 1:
                pygame.draw.circle(screen, black, (circle_x, circle_y), rad)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, white, (circle_x, circle_y), rad)
            elif board[r][c] == 3:
                rect_width = 60
                rect_height = 60
                pad = (70 - rect_width) / 2
                rect_x = 170 + 70 * r + pad
                rect_y = 20 + 70 * c + pad
                
                button("", rect_x, rect_y, rect_width, rect_height, 100, 100, pygame.font.SysFont(None, 50), lambda: puted(r, c))
                #lambda 안넣으면 버튼 안눌려도 함수 실행됨

def show_turn(turn):
    if turn == "흑":
        turn = "black"
    else:
        turn = "white"

    TextSurf, TextRect = text_objects("turn: " + turn, pygame.font.SysFont(None, 30))
    text_x = screen_width / 2
    text_y = screen_height - 10
    TextRect.center = (text_x, text_y)
    screen.blit(TextSurf, TextRect)

def puted(r, c):
    global turn
    global color
    global other

    global leftup
    global up
    global rightup
    global left
    global right
    global leftdown
    global down
    global rightdown

    leftup = 0
    up = 0
    rightup = 0
    left = 0
    right = 0
    leftdown = 0
    down = 0
    rightdown = 0

    reverse(r, c)
    clear_put()

    if turn == "흑":
        turn = "백"
        color = 2
        other = 1
    else:
        turn = "흑"
        color = 1
        other = 2

def game(mode):
    global turn
    global color
    global other

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        
        search_put()

        v_possibility = possibility()
    
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

        screen.fill(lavender)

        fulled = full()
        v_all_reversed = all_reversed()

        draw_board()
        draw_stone()
        show_turn(turn)
        
        if(fulled == False):
            #print("꽉 참: 종료")
            winner = count_score()
            if winner == 1:
                end("black")
            elif winner == 2:
                end("white")
            else:
                end("draw")

        if(v_all_reversed):
            #print("다 뒤집힘: 종료")
            winner = count_score()
            if winner == 1:
                end("black")
            elif winner == 2:
                end("white")
            else:
                end("draw")

        if mode == 1 and turn == "백":
            auto()

        pygame.display.update()

def end(winner):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        
        screen.fill(lavender)

        TextSurf, TextRect = text_objects("winner: " + winner, pygame.font.SysFont(None, 100))
        text_x = screen_width / 2
        text_y = screen_height / 2
        TextRect.center = (text_x, text_y)
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

start()