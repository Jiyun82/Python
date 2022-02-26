import pygame
import random
import pygame.font

pygame.init()

#화면 세팅
screen_width = 600#350
screen_height = 750#700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("지뢰찾기")

#색, 폰트
black = (0, 0, 0)
white = (255, 255, 255)
gray = (195, 195, 195)
red = (235, 86, 86)
blue = (112, 146, 190)
font = pygame.font.SysFont(None, 50)
manual_font = pygame.font.SysFont('malgungothic', 30)
end_font = pygame.font.SysFont('malgungothic', 100)

#변수들
bomb_info = [[0 for col in range(10)] for row in range(20)]#-1은 지뢰 있음, 나머지는 근처 지뢰 개수
look_info = [[0 for col in range(10)] for row in range(20)]#0은 기본 1은 삽으로 파짐 2는 깃발 놓여짐
bomb_index = []#지뢰 있는 자리의 인덱스
side = 35
flag_count = 35
mousepos = [0, 0]
x_start = 125
y_start = 40
end = 0#0은 진행중, 1은 클리어, 2는 실패

#지뢰 생성
while len(bomb_index) < 35:
    rnum = random.randint(0, 199)

    if rnum not in bomb_index:
        bomb_index.append(rnum)

for i in range(35):
    row = bomb_index[i] // 10
    col = bomb_index[i] % 10
    bomb_info[row][col] = -1

#주위 폭탄 개수 파악
for r in range(20):
    for c in range(10):
        bomb_count = 0
        if bomb_info[r][c] != -1:
            for row in range(r - 1, r + 2):
                if 0 <= row < 20:
                    for col in range(c - 1, c + 2):
                        if 0 <= col < 10:
                            if bomb_info[row][col] == -1:
                                bomb_count += 1
            bomb_info[r][c] = bomb_count

#보드 출력(텍스트)
"""
for r in range(20):
    for c in range(10):
        print(bomb_info[r][c], end = " ")
    print("")
"""

def print_bomb_count(bomb_count, x, y):
    text = font.render(str(bomb_count), False, black)
    screen.blit(text, (x + 8, y))

def print_manual():
    text = manual_font.render("좌클: 땅파기  우클: 깃발  남은 깃발: " + str(flag_count), False, black)
    screen.blit(text, (0, 0))

def print_gameover():
    text = end_font.render("Game Over", False, red)
    screen.blit(text, (screen_width * 0.07, screen_height * 0.4))

def print_gameclear():
    text = end_font.render("Game Clear", False, blue)
    screen.blit(text, (screen_width * 0.06, screen_height * 0.4))

def draw_board():
    for r in range(20):
        for c in range(10):
            pygame.draw.rect(screen, black, (x_start + side * c, y_start + side * r, side, side), 3)
            if look_info [r][c] == 0:
                pygame.draw.rect(screen, gray, (x_start + side * c, y_start + side * r, side, side))
            elif look_info[r][c] == 1:
                print_x = x_start + side * c
                print_y = y_start + side * r
                print_bomb_count(bomb_info[r][c], print_x, print_y)
            elif look_info[r][c] == 2:
                pygame.draw.rect(screen, red, (x_start + side * c, y_start + side * r, side, side))
            #이제... 폭탄 개수 나오게 하기

def get_clicked_space_row():
    for r in range(20):
        if y_start + side * r < mousepos[1] < y_start + side * r + side:
            return r

def get_clicked_space_col():
    for c in range(10):
        if x_start + side * c < mousepos[0] < x_start + side * c + side:
            return c

def dig_around_0(r, c):
    again = False
    if bomb_info[r][c] == 0:
        for new_r in range(r - 1, r + 2):
            if 0 <= new_r < 20:
                for new_c in range(c - 1, c + 2):
                    if 0 <= new_c < 10:
                        if look_info[new_r][new_c] == 0:
                            again = True
                        look_info[new_r][new_c] = 1
                        if again:
                            dig_around_0(new_r, new_c)

def gameOver():
    for r in range(20):
        for c in range(10):
            if bomb_info[r][c] == -1:
                rad = side / 2
                circle_x = x_start + side * c + rad
                circle_y = y_start + side * r + rad
                
                pygame.draw.circle(screen, black, (circle_x, circle_y), rad)
    print_gameover()

def check_clear():
    for r in range(20):
        for c in range(10):
            if look_info[r][c] == 0:
                return False
    
    return True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and end == 0:
            clicked_row = get_clicked_space_row()
            clicked_col = get_clicked_space_col()

            if clicked_row != None and clicked_col != None:
                if event.button == 1:#좌 - 삽
                    if look_info[clicked_row][clicked_col] != 2:
                        if bomb_info[clicked_row][clicked_col] == -1:
                            end = 2
                        else:
                            look_info[clicked_row][clicked_col] = 1
                            dig_around_0(clicked_row, clicked_col)
                elif event.button == 3:#우 - 깃발
                    if look_info[clicked_row][clicked_col] == 0 and flag_count > 0:
                        look_info[clicked_row][clicked_col] = 2
                        flag_count -= 1
                    elif look_info[clicked_row][clicked_col] == 2:
                        look_info[clicked_row][clicked_col] = 0
                        flag_count += 1
    
    mousepos[0] = pygame.mouse.get_pos()[0]
    mousepos[1] = pygame.mouse.get_pos()[1]

    screen.fill(white)
    draw_board()
    print_manual()

    cleared = check_clear()
    if cleared:
        end = 1

    if end == 1:
        print_gameclear()
    elif end == 2:
        gameOver()

    pygame.display.update()