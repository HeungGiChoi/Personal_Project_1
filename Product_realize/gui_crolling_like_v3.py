from tkinter import ttk
import tkinter as tk
import youtube_comment_crolling_v1, youtube_comment_like_v2
import threading

# 콤보박스 목록
items = ['유튜브 댓글 크롤링', '유튜브 댓글 좋아요']
# 프레임 목록
frame_li = ['초기화면', '유튜브 댓글 크롤링', '유튜브 댓글 좋아요', '대기화면', '완료화면']
frame_dict = {}

# 메인 클래스 
class MainApp():
    def __init__(self, items, frame_li, frame_dict):
        # 기본 tk 객체 생성
        self.root = tk.Tk()
        self.root.title('유튜브 댓글 크롤링 / 좋아요 click')
        self.root.geometry('400x200+600+200')
        self.items = items
        self.frame_dict = frame_dict
        self.frame_li = frame_li

        # 컨테이너 생성
        self.container = tk.Frame(self.root)
        self.container.pack(side='top', fill='both', expand='True')

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        for i in self.frame_li:
            self.frame_dict[i] = tk.Frame(self.container)
        
        for i in self.frame_dict:
            self.frame_dict[i].grid(row=0, column=0, sticky='nsew')

        self.ComboBox()
        self.comment_crolling()
        self.comment_like_frame()
        self.phose_frame()
        self.complete_frame()

    # 옵션에 따른 frame 전환
    def change_frame(self, option):
        if option in self.frame_dict:
            show_frame = self.frame_dict[option]

            show_frame.tkraise()
        else:
            print('선택된 값은 존재하지 않습니다.')

    # 초기화면
    def ComboBox(self):
        self.combobox = ttk.Combobox(self.frame_dict[self.frame_li[0]], width=20, height=15, values=self.items)
        self.combobox.set('메뉴를 선택하세요')
        self.combobox.pack(pady=20)

        self.button = tk.Button(self.frame_dict[self.frame_li[0]], text='다음', padx=7, pady=5, command=lambda:self.change_frame(self.combobox.get()))
        self.button.pack()

        self.frame_dict[self.frame_li[0]].tkraise()

    # 크롤링 + 화면전환
    def crolling_FrameChange(self, entry):
        self.change_frame('대기화면')

        # threading으로 selenium 작업 진행
        t = threading.Thread(target=youtube_comment_crolling_v1.main, args=(entry, self.change_frame))
        t.start()
    
    # 댓글 크롤링 화면
    def comment_crolling(self):
        self.label = tk.Label(self.frame_dict['유튜브 댓글 크롤링'], text='URL을 입력하세요')
        self.label.pack()
        self.entry_crolling = tk.Entry(self.frame_dict['유튜브 댓글 크롤링'], width=50)
        self.entry_crolling.pack()

        self.button_crolling = tk.Button(self.frame_dict['유튜브 댓글 크롤링'], text='크롤링 실행', padx=15, pady=5, command=lambda:self.crolling_FrameChange(self.entry_crolling.get()))
        self.button_crolling.pack()

    # 댓글 좋아요 + 화면전환
    def like_FrameChange(self, entry_url, entry_ID, entry_PASS):
        self.change_frame('대기화면')

        # threading으로 selenium 작업 진행
        t = threading.Thread(target=youtube_comment_like_v2.main, args=(entry_url, entry_ID, entry_PASS, self.change_frame))
        t.start()

    # 댓글 좋아요 화면
    def comment_like_frame(self):
        tk.Label(self.frame_dict['유튜브 댓글 좋아요'], text='ID, password, URL을 입력하세요').grid(row=0, column=0, columnspan=2, pady=10)
        self.label1 = tk.Label(self.frame_dict['유튜브 댓글 좋아요'], text='ID: ')
        self.label1.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.entry1 = tk.Entry(self.frame_dict['유튜브 댓글 좋아요'], width=20)
        self.entry1.grid(row=1, column=1, sticky='w', padx=10, pady=5)

        self.label2 = tk.Label(self.frame_dict['유튜브 댓글 좋아요'], text='PASS: ')
        self.label2.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.entry2 = tk.Entry(self.frame_dict['유튜브 댓글 좋아요'], width=20)
        self.entry2.grid(row=2, column=1, sticky='w', padx=10, pady=5)

        self.label3 = tk.Label(self.frame_dict['유튜브 댓글 좋아요'], text='URL: ')
        self.label3.grid(row=3, column=0, sticky='w', padx=10, pady=5)
        self.entry3 = tk.Entry(self.frame_dict['유튜브 댓글 좋아요'], width=50)
        self.entry3.grid(row=3, column=1, sticky='ew', padx=10, pady=5)

        self.frame_dict['유튜브 댓글 좋아요'].grid_columnconfigure(1, weight=1)

        self.button_like = tk.Button(self.frame_dict['유튜브 댓글 좋아요'], text='좋아요 누르기 실행', padx=15, pady=5, command=lambda:self.like_FrameChange(self.entry3.get(), self.entry1.get(), self.entry2.get()))
        self.button_like.grid(row=4, column=1, sticky='w', pady=10)

    # 대기화면
    def phose_frame(self):
        self.label_phose = tk.Label(self.frame_dict['대기화면'], text='작업 진행중...')
        self.label_phose.pack(pady=50)

    # 완료 화면
    def complete_frame(self):
        self.label_complete = tk.Label(self.frame_dict['완료화면'], text='작업이 완료되었습니다! ')
        self.label_complete.pack(pady=50)

if __name__ == "__main__":
    application = MainApp(items, frame_li, frame_dict)
    application.root.mainloop()
