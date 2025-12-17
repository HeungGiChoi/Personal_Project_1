from tkinter import ttk
import tkinter as tk
import youtube_comment_crolling_v1, youtube_comment_like_v2
import threading

items = ['유튜브 댓글 크롤링', '유튜브 댓글 좋아요']

# 초기 콤보박스 옵션에 따른 화면전환
def change_frame(option):
    if option in frame_dict:
        show_frame = frame_dict[option]

        show_frame.tkraise()
    else:
        print('선택된 값은 존재하지 않습니다.')

# 크롤링 + 화면전환
def crolling_FrameChange(entry):
    change_frame('대기화면')

    # threading으로 selenium 작업 진행
    t = threading.Thread(target=youtube_comment_crolling_v1.main, args=(entry, change_frame))
    t.start()

# 댓글 좋아요 + 화면전환
def like_FrameChange(entry_url, entry_ID, entry_PASS):
    change_frame('대기화면')

    # threading으로 selenium 작업 진행
    t = threading.Thread(target=youtube_comment_like_v2.main, args=(entry_url, entry_ID, entry_PASS, change_frame))
    t.start()

# 기본 tk 객체 생성
root = tk.Tk()
root.title('유튜브 댓글 크롤링 / 좋아요 click')
root.geometry('400x200+600+200')

# 컨테이너 생성
container = tk.Frame(root)
container.pack(side='top', fill='both', expand='True')

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# frame 딕셔너리
frame_dict = {}
frame_dict["초기화면"] = tk.Frame(container)
frame_dict["유튜브 댓글 크롤링"] = tk.Frame(container)
frame_dict["유튜브 댓글 좋아요"] = tk.Frame(container)
frame_dict["대기화면"] = tk.Frame(container)
frame_dict["완료화면"] = tk.Frame(container)

frame_dict["초기화면"].grid(row=0, column=0, sticky='nsew')
frame_dict["유튜브 댓글 크롤링"].grid(row=0, column=0, sticky='nsew')
frame_dict["유튜브 댓글 좋아요"].grid(row=0, column=0, sticky='nsew')
frame_dict["대기화면"].grid(row=0, column=0, sticky='nsew')
frame_dict["완료화면"].grid(row=0, column=0, sticky='nsew')

# 초기화면
combobox = ttk.Combobox(frame_dict["초기화면"], width=20, height=15, values=items)
combobox.set('메뉴를 선택하세요')
combobox.pack(pady=20)

button = tk.Button(frame_dict["초기화면"], text='다음', padx=7, pady=5, command=lambda:change_frame(combobox.get()))
button.pack()

# 댓글 크롤링 화면
tk.Label(frame_dict['유튜브 댓글 크롤링'], text='URL을 입력하세요').pack()
entry = tk.Entry(frame_dict['유튜브 댓글 크롤링'], width=50)
entry.pack()

button = tk.Button(frame_dict['유튜브 댓글 크롤링'], text='크롤링 실행', padx=15, pady=5, command=lambda:crolling_FrameChange(entry.get()))
button.pack()

# 댓글 좋아요 화면
tk.Label(frame_dict['유튜브 댓글 좋아요'], text='ID, password, URL을 입력하세요').grid(row=0, column=0, columnspan=2, pady=10)
label1 = tk.Label(frame_dict['유튜브 댓글 좋아요'], text='ID: ')
label1.grid(row=1, column=0, sticky='w', padx=10, pady=5)
entry1 = tk.Entry(frame_dict['유튜브 댓글 좋아요'], width=20)
entry1.grid(row=1, column=1, sticky='w', padx=10, pady=5)

label2 = tk.Label(frame_dict['유튜브 댓글 좋아요'], text='PASS: ')
label2.grid(row=2, column=0, sticky='w', padx=10, pady=5)
entry2 = tk.Entry(frame_dict['유튜브 댓글 좋아요'], width=20)
entry2.grid(row=2, column=1, sticky='w', padx=10, pady=5)

label3 = tk.Label(frame_dict['유튜브 댓글 좋아요'], text='URL: ')
label3.grid(row=3, column=0, sticky='w', padx=10, pady=5)
entry3 = tk.Entry(frame_dict['유튜브 댓글 좋아요'], width=50)
entry3.grid(row=3, column=1, sticky='ew', padx=10, pady=5)

frame_dict['유튜브 댓글 좋아요'].grid_columnconfigure(1, weight=1)

button = tk.Button(frame_dict['유튜브 댓글 좋아요'], text='좋아요 누르기 실행', padx=15, pady=5, command=lambda:like_FrameChange(entry3.get(), entry1.get(), entry2.get()))
button.grid(row=4, column=1, sticky='w', pady=10)

# 대기화면
label_phose = tk.Label(frame_dict['대기화면'], text='작업 진행중...')
label_phose.pack(pady=50)

# 완료 화면
label_complete = tk.Label(frame_dict['완료화면'], text='작업이 완료되었습니다! ')
label_complete.pack(pady=50)


frame_dict['초기화면'].tkraise()

root.mainloop()