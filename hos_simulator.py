# import modules
from tkinter import *
import datetime #날짜 생성에 필요한 패키지
import tkinter.messagebox as msgbox #msgbox 사용을 위한 패키지
import sqlite3

####### 통합화면
root = Tk()
root.geometry("1200x600+0+0")

hos_system = Frame(root)
hos_system.pack(side=RIGHT, fill="both", expand=True)

photo1 = PhotoImage(file='./image/paper.png')
right_bott = Frame(hos_system, width=500, height=200)
right_bott.pack(side=BOTTOM, fill="both", expand=True)
reception = Label(right_bott, image=photo1, width=500, height=200)
reception.pack(fill="both")

photo2 = PhotoImage(file='./image/monitor.png')
right_top = Frame(hos_system, width=500, height=400)
right_top.pack(side=TOP, fill="both", expand=True)
tv = Label(right_top, image=photo2, width=500, height=400)
tv.pack(fill="both")

hos_lobby = Frame(root, width=700, height=600 ,bg='BLUE')
hos_lobby.pack(side=LEFT, fill="both", expand=True)

# DB 생성
conn = sqlite3.connect('./manageDB.db', isolation_level=None)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS p_list(id INTEGER PRIMARY KEY AUTOINCREMENT, \
    pname text, pbirth text, psex text, psym text, pdate text)')

# 현재 시점의 날짜
now = datetime.datetime.now()
nowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')

################ 접수처 (오른쪽 아래 화면)
# 접수처 라벨
reception_label = Label(reception, text="<접수처>", font = ('arial 18 bold',16))
reception_label.place(x=200, y=10)

# 예약 정보 입력 라벨 및 텍스트 공간
info_label1 = Label(reception, text="성명", font = ('arial 18 bold',12))
info_text1 = Text(reception, width=23, height=1, state='disabled', bg='LIGHTGRAY')
info_label1.place(x=30, y=60)
info_text1.place(x=100, y=62)
info_label2 = Label(reception, text="생년월일", font = ('arial 18 bold',12))
info_text2 = Text(reception, width=23, height=1, state='disabled', bg='LIGHTGRAY')
info_label2.place(x=20, y=90)
info_text2.place(x=100, y=92)
info_label3 = Label(reception, text="성별", font = ('arial 18 bold',12))
info_text3 = Text(reception, width=23, height=1, state='disabled', bg='LIGHTGRAY')
info_label3.place(x=30, y=120)
info_text3.place(x=100, y=122)
info_label4 = Label(reception, text="증상", font = ('arial 18 bold',12))
info_text4 = Text(reception, width=23, height=1, state='disabled', bg='LIGHTGRAY')
info_label4.place(x=30, y=150)
info_text4.place(x=100, y=152)

def tickbtn():
    bb = cursor.execute("SELECT COUNT(*) FROM p_list")
    vv = Label(ticket_Button, text="대기인원\n"+str(list(bb)[0][0]))
    vv.place(x=16, y=50)
    info_text1.config(state='normal', bg='WHITE')
    info_text2.config(state='normal', bg='WHITE')
    info_text3.config(state='normal', bg='WHITE')
    info_text4.config(state='normal', bg='WHITE')

def chkbtn():
    getinfo1 = info_text1.get("1.0", END).replace('\n', '')
    getinfo2 = info_text2.get("1.0", END).replace('\n', '')
    getinfo3 = info_text3.get("1.0", END).replace('\n', '')
    getinfo4 = info_text4.get("1.0", END).replace('\n', '')
    if getinfo1=='' or getinfo2=='' or  getinfo3=='' or getinfo4=='':
        msgbox.showwarning("주의", "모든 정보를 입력해주세요.")
    else:
        cursor.execute("INSERT INTO p_list(pname, pbirth, psex, psym, pdate) VALUES(?, ?, ?, ?, ?)", (getinfo1, getinfo2, getinfo3, getinfo4, nowDatetime))
        info_text1.config(state='disabled', bg='LIGHTGRAY')
        info_text2.config(state='disabled', bg='LIGHTGRAY')
        info_text3.config(state='disabled', bg='LIGHTGRAY')
        info_text4.config(state='disabled', bg='LIGHTGRAY')

# 티켓 버튼
photo_ticket = PhotoImage(file='./image/ticket.png')
ticket_Button = Button(reception, image=photo_ticket, width=130, height=145, command=tickbtn)
ticket_Button.place(x=350, y=30)

# recep_count = cursor.execute("SELECT COUNT(*) FROM p_list")
# recep_label = Label(ticket_Button, text="대기인원\n"+str(list(recep_count)[0][0]))
# recep_label.place(x=16, y=50)

# 체크 버튼
photo_check = PhotoImage(file='./image/check.png')
check_Button = Button(reception, image=photo_check, width=55, height=50, command=chkbtn)
check_Button.place(x=275, y=120)

# 예약자 목록 TV화면 (오른쪽 위 화면)

# 임시 환자
'''
ppList=(
    ('Park', '19990124', '남자', '알레르기', nowDatetime),
    ('Cho', '19681211', '여자', '편두통', nowDatetime),
    ('An', '19880507', '여자', '외상', nowDatetime),
    ('JY', '19991211', '여자', '두통', nowDatetime),
)
cursor.executemany("INSERT INTO p_list(pname, pbirth, psex, psym, pdate) \
    VALUES(?,?,?,?,?)", ppList)
'''


# 진료 상황 시뮬레이터 (왼쪽 화면)


root.mainloop()
conn.close()