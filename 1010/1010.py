from re import L
import pygame
import random
import pygame.font

pygame.init()

#화면 세팅
screen_width = 1500#1400
screen_height = 750#700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("10x10")

#색
black = (0, 0, 0)
white = (255, 255, 255)
blue = (112, 146, 190)

font = pygame.font.SysFont(None, 50)

#기본 설정
side = 70
score = 0
#dragging = False
holding = False
holding_index = -1#-1, 0, 1, 2: waiting 리스트의 인덱스
puted = False
mousepos = [0, 0]
waiting_x = [180, 180, 1250]
waiting_y = [165, 165 + side * 5, 290]

board = []
for i in range(100):
    board.append(0)

waiting = []#각 waiting 블록들의 모양을 나타내는 숫자(0 ~ 19)를 기록

block1 = [0]
block2_vertical = [0, 10]
block3_vertical = [-10, 0, 10]
block4_vertical = [-10, 0, 10, 20]
block5_vertical = [-20, -10, 0, 10, 20]
block2_horizontal = [0, 1]
block3_horizontal = [-1, 0, 1]
block4_horizontal = [-1, 0, 1, 2]
block5_horizontal = [-2, -1, 0, 1, 2]
block4 = [0, 1, 10, 11]
block_L1 = [-1, 0, 10]
block_L2 = [0, 1, 10]
block_L3 = [-10, 0, 1]
block_L4 = [-10, -1, 0]
block_L5 = [-2, -1, 0, 10, 20]
block_L6 = [0, 1, 2, 10, 20]
block_L7 = [-20, -10, 0, 1, 2]
block_L8 = [-20, -10, -2, -1, 0]
block9 = [-11, -10, -9, -1, 0, 1, 9, 10, 11]
#19개

blocks = [block1, block2_vertical, block3_vertical, block4_vertical, block5_vertical, block2_horizontal, block3_horizontal, block4_horizontal, block5_horizontal, block4, block_L1, block_L2, block_L3, block_L4, block_L5, block_L6, block_L7, block_L8, block9]

def draw_board():
    x = 400
    y = 25

    screen.fill(white)

    for i in range(100):
        row = i // 10
        col = i % 10

        if board[i] == 0:
            pygame.draw.rect(screen, black, (x + side * col, y + side * row, side, side), 3)
        else:
            pygame.draw.rect(screen, blue, (x + side * col, y + side * row, side, side))

def clear_board():
    clear_horizontal = []#row 저장
    clear_vertical = []#col 저장
    for row in range(10):
        count = 0
        for col in range(10):
            i = row * 10 + col
            if board[i] == 1:
                count += 1
            if count == 10:
                clear_horizontal.append(row)
    for col in range(10):
        count = 0
        for row in range(10):
            i = row * 10 + col
            if board[i] == 1:
                count += 1
            if count == 10:
                clear_vertical.append(col)
    
    for row in clear_horizontal:
        for col in range(10):
            i = row * 10 + col
            board[i] = 0
    for col in clear_vertical:
        for row in range(10):
            i = row * 10 + col
            board[i] = 0

def make_waiting():
    global holding_index

    if len(waiting) == 0:
        for i in range(3):
            waiting_index = random.randint(0, len(blocks) - 1)
            waiting.append(waiting_index)

    for i in range(3):
        if i != holding_index:
            draw_waiting(waiting[i], waiting_x[i], waiting_y[i])

def draw_waiting(waiting_index, x, y):
    i = waiting_index#i == 19일때 빈칸 하면 될듯??

    if i == 19:
        return

    pygame.draw.rect(screen, blue, (x, y, side, side))

    if -20 in blocks[i]:
        pygame.draw.rect(screen, blue, (x, y - side * 2, side, side))
    if -11 in blocks[i]:
        pygame.draw.rect(screen, blue, (x - side, y - side, side, side))
    if -10 in blocks[i]:
        pygame.draw.rect(screen, blue, (x, y - side, side, side))
    if -9 in blocks[i]:
        pygame.draw.rect(screen, blue, (x + side, y - side, side, side))
    if -2 in blocks[i]:
        pygame.draw.rect(screen, blue, (x - side * 2, y, side, side))
    if -1 in blocks[i]:
        pygame.draw.rect(screen, blue, (x - side, y, side, side))
    if 1 in blocks[i]:
        pygame.draw.rect(screen, blue, (x + side, y, side, side))
    if 2 in blocks[i]:
        pygame.draw.rect(screen, blue, (x + side * 2, y, side, side))
    if 9 in blocks[i]:
        pygame.draw.rect(screen, blue, (x - side, y + side, side, side))
    if 10 in blocks[i]:
        pygame.draw.rect(screen, blue, (x, y + side, side, side))
    if 11 in blocks[i]:
        pygame.draw.rect(screen, blue, (x + side, y + side, side, side))
    if 20 in blocks[i]:
        pygame.draw.rect(screen, blue, (x, y + side * 2, side, side))

def clear_waiting():
    for i in range(3):
        if waiting[i] != 19:
            return
    else:
        waiting.clear()
        make_waiting()

def collision_box(x, y, index):
    global holding
    global holding_index

    if x < mousepos[0] < x + side and y < mousepos[1] < y + side:
        holding = True
        holding_index = index

def collision(waiting_index, x, y, index):
    global holding
    global holding_index
    i = waiting_index

    if i == 19:
        return
    
    collision_box(x, y, index)

    if -20 in blocks[i]:
        new_x = x
        new_y = y - side * 2
        collision_box(new_x, new_y, index)
    if -11 in blocks[i]:
        new_x = x - side
        new_y = y - side
        collision_box(new_x, new_y, index)
    if -10 in blocks[i]:
        new_x = x
        new_y = y - side
        collision_box(new_x, new_y, index)
    if -9 in blocks[i]:
        new_x = x + side
        new_y = y - side
        collision_box(new_x, new_y, index)
    if -2 in blocks[i]:
        new_x = x - side * 2
        new_y = y
        collision_box(new_x, new_y, index)
    if -1 in blocks[i]:
        new_x = x - side
        new_y = y
        collision_box(new_x, new_y, index)
    if 1 in blocks[i]:
        new_x = x + side
        new_y = y
        collision_box(new_x, new_y, index)
    if 2 in blocks[i]:
        new_x = x + side * 2
        new_y = y
        collision_box(new_x, new_y, index)
    if 9 in blocks[i]:
        new_x = x - side
        new_y = y + side
        collision_box(new_x, new_y, index)
    if 10 in blocks[i]:
        new_x = x
        new_y = y + side
        collision_box(new_x, new_y, index)
    if 11 in blocks[i]:
        new_x = x + side
        new_y = y + side
        collision_box(new_x, new_y, index)
    if 20 in blocks[i]:
        new_x = x
        new_y = y + side * 2
        collision_box(new_x, new_y, index)

def get_board_number():
    x = 400
    y = 25

    for i in range(100):
        row = i // 10
        col = i % 10

        new_x = x + side * col
        new_y = y + side * row

        if new_x < mousepos[0] < new_x + side and new_y < mousepos[1] < new_y + side:
            return i

def isEmpty(board_number, waiting_index):#waiting_index: waiting블록의 모양을 나타내는 번호(0 ~ 14)
    if board_number == None:
        return False
    for i in blocks[waiting_index]:
        before_row = board_number // 10
        check_i = board_number + i
        after_row = check_i // 10
        if -2 <= i <= 2 and before_row != after_row:
            return False
        if check_i < 0 or check_i > 99:
            return False
        if board[check_i] == 1:
            return False
    else:
        return True

def put_block(board_number, waiting_index):
    for i in blocks[waiting_index]:
        board[board_number + i] = 1

def can_put():
    for i in range(3):
        for j in range(100):
            if waiting[i] != 19:
                if isEmpty(j, waiting[i]):
                    return True
    
    return False

def quitgame():
    pygame.quit()

def print_score(score):
    text = font.render("score: " + str(score), False, black)
    screen.blit(text, (1200, 700))

def print_result():
    text = font.render("score: " + str(score), False, black)
    screen.blit(text, (screen_width * 0.5 - 25, screen_height * 0.5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if holding:
                board_number = get_board_number()
                if isEmpty(board_number, waiting[holding_index]):
                    put_block(board_number, waiting[holding_index])
                    score += len(blocks[waiting[holding_index]])
                    waiting[holding_index] = 19
                holding = False
                puted = True
                holding_index = -1

            else:
                for i in range(3):
                    collision(waiting[i], waiting_x[i], waiting_y[i], i)
        
    mousepos[0] = pygame.mouse.get_pos()[0]
    mousepos[1] = pygame.mouse.get_pos()[1]
        
    draw_board()
    make_waiting()
    clear_waiting()
    clear_board()
    print_score(score)
    running = can_put()

    if holding:
        draw_waiting(waiting[holding_index], mousepos[0] - side / 2, mousepos[1] - side / 2)

    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame()
    screen.fill(white)
    print_result()
    pygame.display.update()