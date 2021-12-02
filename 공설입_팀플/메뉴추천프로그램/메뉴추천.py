#파일경로수정해주세요: 23, 190, 246, 300, 327번째 줄

from tkinter import *
import random
from PIL import Image, ImageTk
import pandas as pd
from selenium import webdriver
import time
import warnings
warnings.filterwarnings("ignore")

def show_frame(frame):
    frame.tkraise()
    up_frame.tkraise()

    if frame == worldcup_frame:
        worldCuplist.clear()

#메뉴
menu = ["돈까스", "라면", "우동", "초밥", "덮밥", "짜장면", "짬뽕", "김밥", "떡볶이", "고기", "찌개류", "스파게티", "비빔밥", "피자", "치킨", "햄버거", "닭발"]

#이미지(png파일=https://convertio.co/kr/jpg-gif/ 이미지 크기 조절=https://www.iloveimg.com/ko/resize-image)
imgmenu = {"돈까스":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\1.png",
"라면":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\2.png",
"우동":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\3.png",
"초밥":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\4.png",
"덮밥":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\5.png",
"짜장면":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\6.png",
"짬뽕":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\7.png",
"김밥":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\8.png",
"떡볶이":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\png이미지\\9.png",
"고기":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\10.png",
"찌개류":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\11.png",
"스파게티":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\12.png",
"비빔밥":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\13.png",
"피자":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\14.png",
"치킨":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\15.png",
"햄버거":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\16.png",
"닭발":"C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\17.png"}

#메뉴 받기(카테고리, 올림픽)
Datemenu = []

#클릭 버튼(추천 메뉴 변환)
def ClinkRandom():
    #글로벌로 함수에서 데이터 받기
    global img
    global Datemenu
    global Dateimgfile
    
     #랜덤 함수
    if (len(Datemenu) == 0):
        i = random.randrange(0, len(menu))
        m_menu = menu[i]
        m_ing = imgmenu[m_menu]
    else:
        i = random.randrange(0, len(Datemenu))
        m_menu = Datemenu[i]
        m_ing = imgmenu[m_menu]

    photo2 = ImageTk.PhotoImage(Image.open(m_ing))
    img.configure(image = photo2)
    img.image=photo2
    label1['text'] = "오늘의 점심은 " + m_menu

#월드컵함수
worldCuplist = []
listlen = 0
i = 0
win = "-"

def randomWorldCupMenu(num):
    show_frame(worldcup_frame2)
    if num == 8:
        for i in range(8):
            k = random.choice(menu)
            while k in worldCuplist:#k가 이미 선택되었으면 다시 선택
                k = random.choice(menu)
            worldCuplist.append(k)
    
    elif num == 16:
        for i in range(16):
            k = random.choice(menu)
            while k in worldCuplist:
                k = random.choice(menu)
            worldCuplist.append(k)

    random.shuffle(worldCuplist)
    startRound()

def startRound():
    global listlen 
    global i
    global win
    i = 0
    listlen = int(len(worldCuplist))

    if listlen <= 1:
        win = worldCuplist[0]
        win_label.configure(text = "우승: %s" % (win))
        worldCuplist.clear()
        show_frame(worldcup_frame3)
    
    else:
        if listlen == 2:
            worldcup_label2.configure(text = "결승")
        elif listlen == 4:
            worldcup_label2.configure(text = "준결승")
        else:
            worldcup_label2.configure(text = "%d강"%(listlen))

        left_label.configure(text = worldCuplist[0])
        right_label.configure(text = worldCuplist[1])

        change_image(0, left_photo, left_photo_label)
        change_image(1, right_photo, right_photo_label)

def nextMenu(choice):
    global i
    if choice == 1:
        worldCuplist.remove(worldCuplist[i+1])
    elif choice == 2:
        worldCuplist.remove(worldCuplist[i])
    i += 1

    if i > (listlen / 2) - 1:
        startRound()
    else:
        left_label.configure(text = worldCuplist[i])
        right_label.configure(text = worldCuplist[i+1])
        change_image(i, left_photo, left_photo_label)
        change_image(i+1, right_photo, right_photo_label)

def change_image(i, photo, label):
    m_menu = None
    m_ing = None
    for j in range(len(menu)):
        if worldCuplist[i] == menu[j]:
            m_menu = menu[j]
            m_ing = imgmenu[m_menu]
    
    photo = ImageTk.PhotoImage(Image.open(m_ing))
    label.configure(image = photo)
    label.image = photo

#지도 함수
usermenu = ""
userdetail = ""
userinput = ""
csv_path = ""
df = None

def set_category(name):
    global usermenu
    usermenu = name

    if usermenu == "한식":
        information_label.configure(text = "한식의 종류는\n돼지갈비,돼지족발,냉면,\n김치전골,순대국,소고기국밥,\n닭갈비,쭈꾸미,설렁탕\n ...등이 있습니다\n원하시는 메뉴를 입력해주세요")
    elif usermenu=='중국식':
        information_label.configure(text = "중국식의 종류는\n탕수육,짜장면,짬뽕,어향동고\n...등이 있습니다\n원하시는 메뉴를 입력해주세요")
    elif usermenu == '일식':
        information_label.configure(text = "일식의 종류는\n꼬치,스시,초밥,회\n...등이 있습니다\n원하시는 메뉴를 입력해주세요")
    elif usermenu == '경양식':
        information_label.configure(text = "경양식의 종류는\n돈까스,스테이크,파스타,\n피자,샐러드\n...등이 있습니다\n원하시는 메뉴를 입력해주세요")
    elif usermenu == '분식':
        information_label.configure(text = "분식의 종류는\n빈대떡,국수,도시락,\n칼국수,쌀국수,떡볶이\n...등이 있습니다\n원하시는 메뉴를 입력해주세요")
    elif usermenu == '횟집':
        information_label.configure(text = "횟집의 종류는\n참치회,활어회,생선회,게찜\n...등이 있습니다\n원하시는 메뉴를 입력해주세요")
    elif usermenu == '외국음식전문점(인도태국등)':
        information_label.configure(text = "외국음식의 종류는\n쌀국수,치킨엔칠라다,타코,\n뿌팟봉커리,버터치킨마크니\n...등이 있습니다\n원하시는 메뉴를 입력해주세요")
    elif usermenu == '뷔페식':
        information_label.configure(text = "뷔페식의 종류는\n한중일식,샤브샤브샐러드,\n한식뷔페,샐러드바,초밥 그릴\n...등이 있습니다\n원하시는 메뉴를 입력해주세요")
    elif usermenu == '식육(숯불구이)':
        information_label.configure(text = "식육의 종류는\n차돌박이,갈비탕,돼지갈비,\n소갈비,삼결살\n...등이 있습니다\n원하시는 메뉴를 입력해주세요")

    show_frame(menu_frame)

def set_menu():
    global userdetail
    userdetail = menu_entry.get()
    show_frame(location_frame)

def set_location(name):
    global userinput
    global csv_path
    global df
    userinput = name

    if userinput=='종로구':
        csv_path='C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\jonro.csv'
    elif userinput=='강남구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\gangnam.csv'
    elif userinput == '강동구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\gangdong.csv'
    elif userinput == '강북구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\gangbook.csv'
    elif userinput == '강서구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\gangsu.csv'
    elif userinput == '관악구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\gwanak.csv'
    elif userinput == '광진구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\gwangjin.csv'
    elif userinput == '구로구':
         csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\guro.csv'
    elif userinput == '금천구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\gmcheon.csv'
    elif userinput == '노원구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\nowon.csv'
    elif userinput == '도봉구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\dobong.csv'
    elif userinput == '동대문구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\dongdaemoon.csv'
    elif userinput == '동작구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\dongjak..csv'
    elif userinput == '마포구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\mapo.csv'
    elif userinput == '서대문구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\sudaemoon.csv'
    elif userinput == '서초구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\sucho.csv'
    elif userinput == '성동구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\sungdong.csv'
    elif userinput == '성북구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\sungbook.csv'
    elif userinput == '송파구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\songpa.csv'
    elif userinput == '양천구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\yangcheon.csv'
    elif userinput == '영등포구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\youngdungpo.csv'
    elif userinput == '용산구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\yongsan.csv'
    elif userinput == '은평구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\enpyeong.csv'
    elif userinput == '중구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\joonggu.csv'
    elif userinput == '중랑구':
        csv_path = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\rest\\jongrang.csv'

    df = pd.read_csv(csv_path, sep=',', encoding='CP949')
    df = df[['업소명', '소재지도로명', '업태명', '주된음식', '행정동명', '소재지전화번호']]
    df.columns = ['name', 'address', 'cate1', 'cate2', 'dong', 'phone']
    df=df.loc[(df['cate1']==usermenu)&(df['cate2']==userdetail)]
    df = df.drop_duplicates(['name'], keep='first')
    df['cate_mix'] = df['cate1'] + df['cate2']
    chromedriver = 'C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    df['kakao_keyword'] = df['dong'] + " " + df['name']

    show_frame(result_frame)

    listbox.delete(0, END)
    
    for i, keyword in enumerate(df['kakao_keyword'].tolist()):
        listbox.insert(3 * i + 1, "%d: %s" % (i + 1, keyword))
        #print("이번에 찾을 키워드 :", i+1, f"/ {df.shape[0]} 행", keyword)
        try:
            kakao_map_search_url = f"https://map.kakao.com/?q={keyword}"
            driver.get(kakao_map_search_url)
            time.sleep(1)

            rate = driver.find_element_by_css_selector(
                "#info\.search\.place\.list > li.PlaceItem.clickArea.PlaceItem-ACTIVE > div.rating.clickArea > span.score > em").text
            rateNum = driver.find_element_by_css_selector(
                "#info\.search\.place\.list > li.PlaceItem.clickArea.PlaceItem-ACTIVE > div.rating.clickArea > span.score > a").text
            adr=driver.find_element_by_css_selector(
                "#info\.search\.place\.list > li.PlaceItem.clickArea.PlaceItem-ACTIVE > div.info_item> div.addr>p").text

            listbox.insert(3 * i + 2, "리뷰: %s, 평점: %s" % (rateNum, rate))
            listbox.insert(3 * i + 3, "주소: %s" % adr)

            print("리뷰 " + rateNum + ", 평점 : " + rate + ", 주소 : " + adr )

        except Exception as e1:
            listbox.insert(3 * i + 2, "정보 없음")
            #print("정보 없음")
            pass


#시작
root = Tk()
root.title("")
root.geometry("300x500")
root.resizable = (0, 0)

#상단 바 프레임
up_frame = Frame(root, bg = "white")
up_frame.place(x = 0, y = 0, relwidth = 1)

up_label = Label(up_frame, text = "메뉴 추천 프로그램", bg = "white", font = "NanumGothic 15", pady = 10)
up_label.pack()

#랜덤 메뉴 추천 프레임
random_frame = Frame(root)
random_frame.place(x = 0, rely = 0.1, relwidth = 1, relheight = 0.8)

btn_chu = Button(random_frame, text="추천메뉴 보기", fg="black", bg="white", command=ClinkRandom)
btn_chu.pack(pady = 10)

photo = ImageTk.PhotoImage(Image.open("C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\0.png"))

img = Label(random_frame, image=photo)
img.pack()

label1 = Label(random_frame, text="")
label1.pack()

#월드컵 프레임
worldcup_frame = Frame(root)
worldcup_frame.place(x = 0, rely = 0.1, relwidth = 1, relheight = 0.8)

worldcup_label = Label(worldcup_frame, text = "음식 월드컵", font = "NanumGothic 30")
worldcup_label.place(x = 0, rely = 0.15, relwidth = 1)

button_8 = Button(worldcup_frame, text = "8강", font = "NanumGothic 20", command = lambda: randomWorldCupMenu(8))
button_8.place(relx = 0.4, rely = 0.4)

button_16 = Button(worldcup_frame, text = "16강", font = "NanumGothic 20", command = lambda: randomWorldCupMenu(16))
button_16.place(relx = 0.375, rely = 0.6)

worldcup_frame2 = Frame(root)
worldcup_frame2.place(x = 0, rely = 0.1, relwidth = 1, relheight = 0.8)

worldcup_label2 = Label(worldcup_frame2, text = "-강", font = "NanumGothic 20")
worldcup_label2.place(x = 0, rely = 0.05, relwidth = 1)

left_photo = ImageTk.PhotoImage(Image.open("C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\1.png"))
right_photo = ImageTk.PhotoImage(Image.open("C:\\Users\\jiyun\\Documents\\학교\\공설입\\팀플\\메뉴추천프로그램\\png이미지\\1.png"))
left_photo_label = Label(worldcup_frame2, image = left_photo)
right_photo_label = Label(worldcup_frame2, image = right_photo)
left_photo_label.place(relx = 0, rely = 0.2, relwidth = 0.5, relheight = 0.3)
right_photo_label.place(relx = 0.5, rely = 0.2, relwidth = 0.5, relheight = 0.3)

left_label = Label(worldcup_frame2, text = "음식1", font = "NanumGothic 20")
left_label.place(relx = 0.1, rely = 0.6)

right_label = Label(worldcup_frame2, text = "음식2", font = "NanumGothic 20")
right_label.place(relx = 0.65, rely = 0.6)

left_button = Button(worldcup_frame2, text = "선택", font = "NanumGothic 20", command = lambda: nextMenu(1))
left_button.place(relx = 0.1, rely = 0.8)

right_button = Button(worldcup_frame2, text = "선택", font = "NanumGothic 20", command = lambda: nextMenu(2))
right_button.place(relx = 0.65, rely = 0.8)

worldcup_frame3 = Frame(root)
worldcup_frame3.place(x = 0, rely = 0.1, relwidth = 1, relheight = 0.8)

win_label = Label(worldcup_frame3, text = "우승: %s" % (win), font = "NanumGothic 20")
win_label.place(relx = 0, rely = 0.4, relwidth = 1)

#지도 프레임
category_frame = Frame(root)#카테고리선택프레임
category_frame.place(x = 0, rely = 0.1, relwidth = 1, relheight = 0.8)
category_label = Label(category_frame, text = "[카테고리를 선택해주세요]", font = "NanumGothic 18")
category_label.grid(row = 0, column = 0, columnspan = 12, pady = 30)

kor_button = Button(category_frame, text = "한식", font = "NanumGothic 11", command = lambda: set_category("한식"))
ch_button = Button(category_frame, text = "중국식", font = "NanumGothic 11", command = lambda: set_category("중국식"))
jp_button = Button(category_frame, text = "일식", font = "NanumGothic 11", command = lambda: set_category("일식"))
nth_button = Button(category_frame, text = "경양식", font = "NanumGothic 11", command = lambda: set_category("경양식"))
snack_button = Button(category_frame, text = "분식", font = "NanumGothic 11", command = lambda: set_category("분식"))
fish_button = Button(category_frame, text = "횟집", font = "NanumGothic 11", command = lambda: set_category("횟집"))
buffet_button = Button(category_frame, text = "뷔페식", font = "NanumGothic 11", command = lambda: set_category("뷔페식"))
foreign_button = Button(category_frame, text = "외국음식전문점(인도태국등)", font = "NanumGothic 11", command = lambda: set_category("외국음식전문점(인도태국등)"))
meat_button = Button(category_frame, text = "식육(숯불구이)", font = "NanumGothic 11", command = lambda: set_category("식육(숯불구이)"))

kor_button.grid(row = 1, column = 0, columnspan = 3, sticky = "nsew", ipady = 10, pady = 5)
ch_button.grid(row = 1, column = 3, columnspan = 3, sticky = "nsew", ipady = 10, pady = 5)
jp_button.grid(row = 1, column = 6, columnspan = 3, sticky = "nsew", ipady = 10, pady = 5)
nth_button.grid(row = 1, column = 9, columnspan = 3, sticky = "nsew", ipady = 10, pady = 5)
snack_button.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew", ipady = 10, pady = 5)
fish_button.grid(row = 2, column = 4, columnspan = 4, sticky = "nsew", ipady = 10, pady = 5)
buffet_button.grid(row = 2, column = 8, columnspan = 4, sticky = "nsew", ipady = 10, pady = 5)
foreign_button.grid(row = 3, column = 0, columnspan = 8, sticky = "nsew", ipady = 10, pady = 5)
meat_button.grid(row = 3, column = 8, columnspan = 4, sticky = "nsew", ipady = 10, pady = 5)

menu_frame = Frame(root)#메뉴입력프레임
menu_frame.place(x = 0, rely = 0.1, relwidth = 1, relheight = 0.8)

information_label = Label(menu_frame, text = "-의 종류는\n-...등이\n있습니다\n원하시는 메뉴를 입력해주세요", font = "NanumGothic 15")
information_label.place(x = 0, rely = 0.05, relwidth = 1)

menu_entry = Entry(menu_frame)
menu_entry.place(relx = 0.1, rely = 0.5, relwidth = 0.6, relheight = 0.1)

search_button = Button(menu_frame, text = "검색", command = set_menu)
search_button.place(relx = 0.7, rely = 0.5, relwidth = 0.2, relheight = 0.1)

location_frame = Frame(root)#위치 선택 프레임
location_frame.place(x = 0, rely = 0.1, relwidth = 1, relheight = 0.8)

information_label2 = Label(location_frame, text = "위치를 선택해주세요")
information_label2.grid(row = 0, column = 0, columnspan = 5, sticky = "nsew")

button0 = Button(location_frame, text = "강남구", font = "NanumGothic 10", command = lambda: set_location("강남구"))
button1 = Button(location_frame, text = "강동구", font = "NanumGothic 10", command = lambda: set_location("강동구"))
button2 = Button(location_frame, text = "강북구", font = "NanumGothic 10", command = lambda: set_location("강북구"))
button3 = Button(location_frame, text = "강서구", font = "NanumGothic 10", command = lambda: set_location("강서구"))
button4 = Button(location_frame, text = "관악구", font = "NanumGothic 10", command = lambda: set_location("관악구"))
button5 = Button(location_frame, text = "광진구", font = "NanumGothic 10", command = lambda: set_location("광진구"))
button6 = Button(location_frame, text = "구로구", font = "NanumGothic 10", command = lambda: set_location("구로구"))
button7 = Button(location_frame, text = "금천구", font = "NanumGothic 10", command = lambda: set_location("금천구"))
button8 = Button(location_frame, text = "노원구", font = "NanumGothic 10", command = lambda: set_location("노원구"))
button9 = Button(location_frame, text = "도봉구", font = "NanumGothic 10", command = lambda: set_location("도봉구"))
button10 = Button(location_frame, text = "동대문구", font = "NanumGothic 10", command = lambda: set_location("동대문구"))
button11 = Button(location_frame, text = "동작구", font = "NanumGothic 10", command = lambda: set_location("동작구"))
button12 = Button(location_frame, text = "마포구", font = "NanumGothic 10", command = lambda: set_location("마포구"))
button13 = Button(location_frame, text = "서대문구", font = "NanumGothic 10", command = lambda: set_location("서대문구"))
button14 = Button(location_frame, text = "서초구", font = "NanumGothic 10", command = lambda: set_location("서초구"))
button15 = Button(location_frame, text = "성동구", font = "NanumGothic 10", command = lambda: set_location("성동구"))
button16 = Button(location_frame, text = "성북구", font = "NanumGothic 10", command = lambda: set_location("성북구"))
button17 = Button(location_frame, text = "송파구", font = "NanumGothic 10", command = lambda: set_location("송파구"))
button18 = Button(location_frame, text = "양천구", font = "NanumGothic 10", command = lambda: set_location("양천구"))
button19 = Button(location_frame, text = "영등포구", font = "NanumGothic 10", command = lambda: set_location("영등포구"))
button20 = Button(location_frame, text = "용산구", font = "NanumGothic 10", command = lambda: set_location("용산구"))
button21 = Button(location_frame, text = "은평구", font = "NanumGothic 10", command = lambda: set_location("은평구"))
button22 = Button(location_frame, text = "종로구", font = "NanumGothic 10", command = lambda: set_location("종로구"))
button23 = Button(location_frame, text = "중구", font = "NanumGothic 10", command = lambda: set_location("중구"))
button24 = Button(location_frame, text = "중랑구", font = "NanumGothic 10", command = lambda: set_location("중랑구"))

gu_ipadx = 2.4

button0.grid(row = 1, column = 0, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button1.grid(row = 1, column = 1, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button2.grid(row = 1, column = 2, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button3.grid(row = 1, column = 3, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button4.grid(row = 1, column = 4, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button5.grid(row = 2, column = 0, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button6.grid(row = 2, column = 1, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button7.grid(row = 2, column = 2, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button8.grid(row = 2, column = 3, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button9.grid(row = 2, column = 4, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button10.grid(row = 3, column = 0, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button11.grid(row = 3, column = 1, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button12.grid(row = 3, column = 2, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button13.grid(row = 3, column = 3, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button14.grid(row = 3, column = 4, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button15.grid(row = 4, column = 0, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button16.grid(row = 4, column = 1, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button17.grid(row = 4, column = 2, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button18.grid(row = 4, column = 3, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button19.grid(row = 4, column = 4, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button20.grid(row = 5, column = 0, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button21.grid(row = 5, column = 1, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button22.grid(row = 5, column = 2, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button23.grid(row = 5, column = 3, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)
button24.grid(row = 5, column = 4, sticky = "nsew", ipady = 10, ipadx = gu_ipadx)

result_frame = Frame(root)#검색 결과 출력 프레임
result_frame.place(x = 0, rely = 0.1, relwidth = 1, relheight = 0.8)

result_label = Label(result_frame, text = "<모범음식점 검색 결과>", font = "NanumGothic 20")
result_label.place(relx = 0, rely = 0.05, relwidth = 1)

scroll_frame = Frame(result_frame)
scroll_frame.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.8)

scrollbar = Scrollbar(scroll_frame)
scrollbar.pack(side = "right", fill = "y")

listbox = Listbox(scroll_frame, yscrollcommand = scrollbar.set, activestyle = "none", font = "NanumGothic 13")
listbox.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

scrollbar["command"] = listbox.yview

#하단 버튼 프레임
down_frame = Frame(root)
down_frame.place(x = 0, rely = 0.9)

down_frame.columnconfigure(0, weight = 1)
down_frame.columnconfigure(1, weight = 1)
down_frame.columnconfigure(2, weight = 1)

random_button = Button(down_frame, text = "랜덤", font = "NanumGothic 15", command = lambda: show_frame(random_frame))
random_button.grid(row = 0, column = 0, ipadx = 22, ipady = 5)

map_button = Button(down_frame, text = "검색", font = "NanumGothic 15", command = lambda: show_frame(category_frame))
map_button.grid(row = 0, column = 1, ipadx = 22, ipady = 5)

worldcup_button = Button(down_frame, text = "월드컵", font = "NanumGothic 15", command = lambda: show_frame(worldcup_frame))
worldcup_button.grid(row = 0, column = 2, ipadx = 15, ipady = 5)

show_frame(random_frame)

root.mainloop()