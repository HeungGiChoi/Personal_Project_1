from tkinter import ttk
import tkinter as tk

# Tk 객체 생성
root = tk.Tk()

# 창 제목 설정
root.title("유튜브 댓글 크롤링 / 좋아요 click")

# 창 크기 설정
root.geometry("400x200+500+150")

# 창 크기 변경 불가
root.resizable(False, False)

frame1 = tk.Frame(root, relief='solid', bd=2)
frame1.pack(side='left', fill='both', expand=True)
frame2 = tk.Frame(root, relief='solid', bd=2)
frame2.pack(side='right', fill='both', expand=True)

label1 = tk.Label(frame1, text='frame1')
label1.pack()
label2 = tk.Label(frame2, text='frame2')
label2.pack()

# label = tk.Label(root, text='frame 테스트')
# label.pack()

# frame = tk.Frame(root)
# frame.pack()

root.mainloop()