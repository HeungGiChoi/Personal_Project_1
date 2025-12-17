from tkinter import ttk
import tkinter as tk
import youtube_comment_crolling_v1, youtube_comment_like_v2
import threading

# 콤보박스 목록
items = ['유튜브 댓글 크롤링', '유튜브 댓글 좋아요']
# 프레임 목록
frame_li = ['초기화면', '유튜브 댓글 크롤링', '유튜브 댓글 좋아요', '대기화면', '완료화면']
frame_dict = {}

# 초기화 + 첫번째 화면
class FirstFrame():
    root = tk.Tk()

    def __init__(self, items, frame_li, frame_dict):
        # 기본 tk 객체 생성
        self.items = items
        self.frame_dict = frame_dict
        self.root.title('유튜브 댓글 크롤링 / 좋아요 click')
        self.root.geometry('400x200+600+200')

        # 컨테이너 생성
        container = tk.Frame(self.root)
        container.pack(side='top', fill='both', expand='True')

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for i in frame_li:
            self.frame_dict[i] = tk.Frame(container)
        
        for i in self.frame_dict:
            self.frame_dict[i].grid(row=0, column=0, sticky='nsew')

    # 초기화면
    def ComboBox(self):
        combobox = ttk.Combobox(self.frame_dict[0], width=20, height=15, values=self.items)
        combobox.set('메뉴를 선택하세요')
        combobox.pack(pady=20)

        button = tk.Button(self.frame_dict[0], text='다음', padx=7, pady=5, command=lambda:self.change_frame(combobox.get()))
        button.pack()

        self.frame_dict[0].tkraise()
    
    # 옵션에 따른 frame 전환
    def change_frame(self, option):
        if option in self.frame_dict:
            show_frame = self.frame_dict[option]

            show_frame.tkraise()
        else:
            print('선택된 값은 존재하지 않습니다.')
    
    root.mainloop()


FirstFrame(items, frame_li, frame_dict)
FirstFrame.ComboBox()

