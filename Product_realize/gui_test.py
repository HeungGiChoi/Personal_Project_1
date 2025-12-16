from tkinter import ttk
import tkinter as tk

def click():
    print('안녕하세요')

def click2():
    button.config(text='성공입니다.')
    # print('성공입니다.')

# Tk 객체 생성
root = tk.Tk()

# 창 제목 설정
root.title("유튜브 댓글 크롤링 / 좋아요 click")

# 창 크기 설정
root.geometry("400x200+500+150")

# 창 크기 변경 불가
root.resizable(False, False)

# 드롭다운 선택 목록
items = ['유튜브 영상 댓글 크롤링', '유튜브 영상 댓글 좋아요']

# 라벨
label = tk.Label(root, text='기능 선택')
label.pack()

combobox = ttk.Combobox(root, width=20, height=15, values=items)
combobox.pack()
combobox.set('선택')

# 엔트리
entry = tk.Entry(root,)
entry.pack()

# 버튼
button = tk.Button(root, text='다음', pady=10, padx=10)
button.pack()

# label_2 = tk.Label(root, text='댓글 크롤링이 완료되었습니다!')
# label_2.pack()

# mainloop 실행
root.mainloop()
# 출처: https://gangdonggil.tistory.com/128 [개발_노트:티스토리]