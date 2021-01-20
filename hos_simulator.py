# import modules
from tkinter import *
import datetime #날짜 생성에 필요한 패키지
import sqlite3

# 통합화면
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

# 접수처 (오른쪽 아래 화면)


# 예약자 목록 TV화면 (오른쪽 위 화면)
# 임시 환자
ppList=(
    ('Park', '19990124', '남자', '알레르기', nowDatetime),
    ('Cho', '19681211', '여자', '편두통', nowDatetime),
    ('An', '19880507', '여자', '외상', nowDatetime),
    #('JY', '19991211', '여자', '두통', nowDatetime),
)
#cursor.executemany("INSERT INTO p_list(pname, pbirth, psex, psym, pdate) \
#    VALUES(?,?,?,?,?)", ppList)

#cursor.execute("INSERT INTO p_list(pname, pbirth, psex, psym, pdate) \
#    VALUES(?,?,?,?,?)", ('Lee', '20000101', '남자', '화상', nowDatetime))


wait_list1 = Label(tv, text = "대기번호", font = ('arial 18 bold'))
wait_list1.place(x=70, y=45)

wait_list1 = Label(tv, text = "이름", font = ('arial 18 bold'))
wait_list1.place(x=185, y=45)

wait_list1 = Label(tv, text = "성별", font = ('arial 18 bold'))
wait_list1.place(x=260, y=45)

wait_list1 = Label(tv, text = "증상", font = ('arial 18 bold'))
wait_list1.place(x=340, y=45)


# 진료 상황 시뮬레이터 (왼쪽 화면)

conn.close()
root.mainloop()