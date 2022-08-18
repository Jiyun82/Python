import pygame
import time
import random
import copy

#기본 세팅

score = 0
recentTime = 0 #fall한 가장 최근의 시간
makeNew = True #새로운 블록 생성할지 여부
tick = 1 #텀

side = 30 #한 칸의 변 30

screenWidth = 14 * side #스크린 가로길이, 20칸
screenHeight = 24 * side #스크린 세로길이, 24칸
screenSize = (screenWidth, screenHeight) #스크린 크기

gameScreenX = 2 * side #게임화면 x좌표, 2번째 칸에서 시작
gameScreenY = 2 * side #게임화면 y좌표, 2번째 칸에서 시작
gameScreenXY = (gameScreenX, gameScreenY) #게임화면 좌표
gameScreenWidth = 10 * side #게임화면 가로길이, 10칸
gameScreenHeight = 20 * side #게임화면 세로길이, 20칸
gameScreenSize = (gameScreenWidth, gameScreenHeight) #게임화면 크기, 10 * 20

white = (255, 255, 255)
black = (0, 0, 0)

blockMatrix = [] #row20, col10
for i in range(20):
    blockMatrix.append([0]*10)

newBlockRC = [] #새로 생성된 블록의 행,열을 저장하는 리스트
#newBlockRC[i][0]: i번째 row, newBlockRC[i][1]: i번째 col
newBlockAngle = 0
originRC = [] #새로 생성된 블록의 처음 위치를 저장하는 리스트
rotatedRC = [] #회전 후의 위치를 저장할 리스트

#blockMatrix에서 새로운 블록을 제거(0으로 변경)
def RemoveNew():
    for  r in range(20):
        for c in range(10):
            #[r, c]가 newBlockRC에 포함된다면 0으로 바꾸기
            if [r, c] in newBlockRC:
                blockMatrix[r][c] = 0

#newBlockRC 애들을 다시 blockMatrix에 매핑
def AddNew():  
    for r in range(20):
        for c in range(10):
            if [r, c] in newBlockRC:
                blockMatrix[r][c] = 1

#새로 생성된 블록 밑에 비었는지 여부 판단
def CanFall_new():
    global makeNew
    LowerRC = [] #가장 낮은 블록들의 행, 열 저장

    #가장 낮은 블록들을 LowerRC에 저장
    for col in range(10):
        LowerRow = 0
        size = len(newBlockRC)
        for i in range(size):
            if col == newBlockRC[i][1] and newBlockRC[i][0] > LowerRow: #지금 체크하고 있는 칸의 칼럼이 col일때만!!
                LowerRow = newBlockRC[i][0]
        LowerRC.append([LowerRow, col])

    #LowerRC의 칸들 밑에 공간 있는지 체크할거임
    size = len(LowerRC)
    for i in range(size):
        rowForCheck = LowerRC[i][0]
        colForCheck = LowerRC[i][1]
        if rowForCheck + 1 >= 20 or blockMatrix[rowForCheck+1][colForCheck] == 1: # 밑에 공간이 없다면 바로 0리턴
            makeNew = True
            return 0
    return 1 #아니라면 1리턴

#새로 생성된 블록
#밑에서부터 확인해서 아래가 빈칸이면...
def Fall_new():
    canFall = CanFall_new()
    if canFall == 0: #떨어질 수 없다면 0 리턴하고 종료
        return 0
    #아니라면 newBlockRC 애들을 한칸씩 밑으로 이동.

    RemoveNew()
    
    #newBlockRC 애들을 한 칸씩 밑으로 옮김
    size = len(newBlockRC)
    for i in range(size):
        newBlockRC[i][0] += 1

    AddNew()

#새로 생성된 블록이 왼쪽으로 이동 가능한지 판단
#모든 가장 왼쪽의 블록들 왼쪽에 공간이 있다면 가능
#모든 가장 왼쪽의 블록들 리스트를 만들고, 그 리스트의 요소들의 왼쪽에 공간이 있는지 확인
def CanGoLeft():
    leftRC = [] #가장 왼쪽의 블록들 리스트
    
    #가장 왼쪽의 칸들을 leftRC에 저장
    for row in range(20):
        leftCol = 10
        for col in range(10):
            if col < leftCol and [row, col] in newBlockRC:
                leftCol = col
        if leftCol != 10:
            leftRC.append([row, leftCol])
    
    size = len(leftRC)
    for i in range(size):
        rowForCheck = leftRC[i][0]
        colForCheck = leftRC[i][1]
        if colForCheck - 1 < 0:
            return 0
        if blockMatrix[rowForCheck][colForCheck-1] == 1:
            return 0
    return 1

def MoveLeft():
    if CanGoLeft() == 0:
        return 0

    RemoveNew()

    #newBlockRC 애들을 한 칸씩 왼쪽으로 옮김
    size = len(newBlockRC)
    for i in range(size):
        newBlockRC[i][1] -= 1

    AddNew()

    return 1

def CanGoRight():
    rightRC = []

    #row가 newBlockRC에 포함되는지 확인해야함
    for row in range(20):
        rightCol = -1
        for col in range(10):
            if col > rightCol and [row, col] in newBlockRC:
                rightCol = col
        if rightCol != -1:
            rightRC.append([row, rightCol])
    
    size = len(rightRC)
    for i in range(size):
        rowForCheck = rightRC[i][0]
        colForCheck = rightRC[i][1]

        if colForCheck + 1 > 9:
            return 0
        if blockMatrix[rowForCheck][colForCheck+1] == 1:
            return 0
    return 1

def MoveRight():
    if CanGoRight() == 0:
        return 0
    
    RemoveNew()

    #newBlockRC 애들 한 칸씩 오른쪽으로 옮김
    size = len(newBlockRC)
    for i in range(size):
        newBlockRC[i][1] +=1
    
    AddNew()

    return 1

#배경 그리기
def DrawBackground():
    pygame.draw.rect(screen, white, (gameScreenXY, gameScreenSize), 1)

#blockMatrix를 바탕으로 1이면 흰색, 0이면 검정색으로 사각형 그리기
def DrawBlock():
    for r in range(20):
        for c in range(10):
            if blockMatrix[r][c] == 1:
                pygame.draw.rect(screen, white, (gameScreenX + c * side, gameScreenY + r * side, side, side))
            else:
                pygame.draw.rect(screen, black, (gameScreenX + c * side, gameScreenY + r * side, side, side))

#tick초가 지났는지 체크하고 recentTime을 재설정
def CheckTime():
    global tick
    global recentTime
    currentTime = time.time()
    if currentTime - recentTime >= tick:
        recentTime = currentTime
        return 1
    return 0

#새로운 블록 생성하기
def MakeNewBlock():
    global makeNew
    global newBlockRC
    global newBlockAngle
    global originRC
    global tick

    if makeNew == False:
        return

    form = random.randint(0, 6)
    if form == 0:#정사각형
        originRC = [[[0, 4], [0, 5], [1, 4], [1, 5]]]
        newBlockAngle = 0
    elif form == 1:#1자 모양
        originRC = [[[0, 4], [1, 4], [2, 4], [3, 4]], [[0, 3], [0, 4], [0, 5], [0, 6]]]
        newBlockAngle = random.randint(0, 1)
    elif form == 2:#ㅗ모양
        originRC = [[[0, 4], [1, 4], [1, 5], [2, 4]], [[0, 4], [0, 5], [0, 6], [1, 5]], [[0, 5], [1, 4], [1, 5], [2, 5]],[[0, 5], [1, 4], [1, 5], [1, 6]]]
        newBlockAngle = random.randint(0, 3)
    elif form == 3:#z 반대
        originRC = [[[0, 4], [1, 4], [1, 5], [2, 5]], [[0, 4], [0, 5], [1, 3], [1, 4]]]
        newBlockAngle = random.randint(0, 1)
    elif form == 4:#z
        originRC = [[[0, 5], [1, 4], [1, 5], [2, 4]], [[0, 3], [0, 4], [1, 4], [1, 5]]]
        newBlockAngle = random.randint(0, 1)
    elif form == 5:#ㄴ
        originRC = [[[0, 4], [0, 5], [1, 4], [2, 4]], [[0, 3], [0, 4], [0, 5], [1, 5]], [[0, 5], [1, 5], [2, 4], [2, 5]], [[0, 3], [1, 3], [1, 4], [1, 5]]]
        newBlockAngle = random.randint(0, 3)
    elif form == 6:#ㄱ
        originRC = [[[0, 4], [0, 5], [1, 5], [2, 5]], [[0, 5], [1, 3], [1, 4], [1, 5]], [[0, 4], [1, 4], [2, 4], [2, 5]], [[0, 3], [0, 4], [0, 5], [1, 3]]]
        newBlockAngle = random.randint(0, 3)
    
    CanMake(originRC[newBlockAngle])

    newBlockRC = copy.deepcopy(originRC[newBlockAngle])
    AddNew()
    makeNew = False

    if tick > 0.2:
        tick -= 0.01

#회전 가능 여부 판단
#현재 위치 - 처음 위치 + 다음 모양의 처음 위치 = 회전 후의 위치
#newBlockAngle
def CanRotate():
    global rotatedRC #회전 후의 위치
    rotatedRC = []
    numberOfForm = len(originRC) #모양의 개수
    nextAngle = (newBlockAngle + 1) % numberOfForm

    size = len(newBlockRC)
    for i in range(size):
        rotatedRow = newBlockRC[i][0] - originRC[newBlockAngle][i][0] + originRC[nextAngle][i][0]
        rotatedCol = newBlockRC[i][1] - originRC[newBlockAngle][i][1] + originRC[nextAngle][i][1]
        rotatedRC.append([rotatedRow, rotatedCol])

    for i in range(size):
        rotatedRow = rotatedRC[i][0]
        rotatedCol = rotatedRC[i][1]
        if rotatedRow > 19 or rotatedRow < 0 or rotatedCol > 9 or rotatedCol < 0: #화면 밖으로 넘어가면
            return 0
        if blockMatrix[rotatedRow][rotatedCol] == 1 and ([rotatedRow, rotatedCol] not in newBlockRC): #회전 후 위치에 공간이 없고, 그 위치가 회전 전 위치가 아니라면
            return 0
    
    return 1

def Rotate():
    if CanRotate() == 0:
        return
    global newBlockRC
    global newBlockAngle

    RemoveNew()
    newBlockRC = copy.deepcopy(rotatedRC)
    newBlockAngle = (newBlockAngle + 1) % len(originRC)
    AddNew()

def ClearLine(row):
    global score
    global makeNew

    for col in range(10):
        blockMatrix[row][col] = 0

    score += 10
    makeNew = True
    DropBlock()

#라인 체크
def CheckLine():
    row = 19
    #for row in range(19, -1, -1):
    while row > -1:
        clearThisLine = True
        for col in range(10):
            if blockMatrix[row][col] == 0:
                clearThisLine = False
            if col == 9: #라인 지우면 그 라인 또 검사해야 함
                if clearThisLine == True:
                    ClearLine(row)
                else:
                    row -= 1

#라인 체크 후 실행할 것
#블럭 아래로 내림
def DropBlock():
    for row in range(19, -1, -1):
        for col in range(10):
            clearThisLine = True
            if blockMatrix[row][col] == 1:
                clearThisLine = False
            elif clearThisLine == True and col == 9 and row - 1 >= 0:
                blockMatrix[row] = copy.deepcopy(blockMatrix[row-1])
                for c in range(10):
                    blockMatrix[row-1][c] = 0

def PrintScore():
    font = pygame.font.SysFont(None, 30)
    scoreStr = "SCORE: " + str(score)
    text = font.render(scoreStr, True, white)
    screen.blit(text, (50, screenHeight - 50))

def CanMake(form):
    global running
    size = len(form)
    for i in range(size):
        row = form[i][0]
        col = form[i][1]
        if blockMatrix[row][col] == 1:
            running = False

def PrintEnd():
    font = pygame.font.SysFont(None, 30)
    endStr = "GAME OVER... SCORE: " + str(score)
    text = font.render(endStr, True, white)
    screen.blit(text, (50, 200))

def PrintMatrix():
    for row in range(20):
        for col in range(10):
            print(blockMatrix[row][col], end = "")
        print()
    print()

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Tetris")

recentTime = time.time() #recentTime에 현재 시간을 저장
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Fall_new()
            if event.key == pygame.K_LEFT:
                MoveLeft()
            if event.key == pygame.K_RIGHT:
                MoveRight()
            if event.key == pygame.K_SPACE:
                Rotate()
    
    screen.fill(black)
    if makeNew == True:
        CheckLine()
        MakeNewBlock()
    if CheckTime() == 1:
        Fall_new()
    DrawBlock()
    DrawBackground()
    PrintScore()
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill(black)
    PrintEnd()
    pygame.display.update()


#종료조건추가