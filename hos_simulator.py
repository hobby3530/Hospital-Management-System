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
reception = Frame(hos_system, width=500, height=200)
reception.pack(side=BOTTOM, fill="both", expand=True)
w1 = Label(reception, image=photo1, width=500, height=200)
w1.pack(fill="both")

photo2 = PhotoImage(file='./image/monitor.png')
tv = Frame(hos_system, width=500, height=400)
tv.pack(side=TOP, fill="both", expand=True)
w2 = Label(tv, image=photo2, width=500, height=400)
w2.pack(fill="both")

hos_lobby = Frame(root, width=700, height=600 ,bg='BLUE')
hos_lobby.pack(side=LEFT, fill="both", expand=True)

root.mainloop()

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
    ('JY', '19991211', '여자', '두통', nowDatetime),
)
cursor.executemany("INSERT INTO p_list(pname, pbirth, psex, psym, pdate) \
    VALUES(?,?,?,?,?)", ppList)

conn.close()

# 진료 상황 시뮬레이터 (왼쪽 화면)


