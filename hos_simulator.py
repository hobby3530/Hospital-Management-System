# import modules
from tkinter import *
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

root.mainloop()

# DB 생성
conn = sqlite3.connect('./manageDB.db', isolation_level=None)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS p_list(id INTEGER PRIMARY KEY AUTOINCREMENT, \
    pname text, pbirth text, psex text, psym text)')

# 접수처 (오른쪽 아래 화면)


# 예약자 목록 TV화면 (오른쪽 위 화면)


# 진료 상황 시뮬레이터 (왼쪽 화면)


