import youtube_comment_crolling_v1, youtube_comment_like_v2
from tkinter import ttk
import tkinter as tk

items = ['유튜브 댓글 크롤링', '유튜브 댓글 좋아요']

root = tk.Tk()
root.title('유튜브 댓글 크롤링 / 좋아요 작업 프로그램')
root.geometry("430x250+500+150")
root.resizable(False, False)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

frame1.grid(row=0, column=0, sticky='nsew')
frame2.grid(row=0, column=0, sticky='nsew')

combobox = ttk.Combobox(frame1, width=20, height=15, values=items)
combobox.set('선택')
combobox.pack()

frame1_button = tk.Button(frame1, text='다음', padx=7, pady=5)
frame1_button.pack()

root.mainloop()