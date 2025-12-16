from tkinter import ttk
import tkinter as tk

def openFrame(frame):
    frame.tkraise()

# Tk 객체 생성
root = tk.Tk()

# 창 제목 설정
root.title("유튜브 댓글 크롤링 / 좋아요 click")

# 창 크기 설정
root.geometry("400x200+500+150")

# 창 크기 변경 불가
root.resizable(False, False)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

frame1.grid(row=0, column=0, sticky='nsew')
frame2.grid(row=0, column=0, sticky='nsew')
frame3.grid(row=0, column=0, sticky='nsew')

btframe1 = tk.Button(frame3,
                     text='change to Frame1',
                     padx=10,
                     pady=10,
                     command=lambda:[openFrame(frame1)])

btframe2 = tk.Button(frame1,
                     text='change to Frame2',
                     padx=10,
                     pady=10,
                     command=lambda:[openFrame(frame2)])

btframe3 = tk.Button(frame2,
                     text='change to Frame3',
                     padx=10,
                     pady=10,
                     command=lambda:[openFrame(frame3)])
                    
btframe1.pack()
btframe2.pack()
btframe3.pack()

openFrame(frame1)

root.mainloop()