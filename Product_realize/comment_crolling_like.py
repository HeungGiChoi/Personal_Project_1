import youtube_comment_crolling_v1, youtube_comment_like_v2
import sys
import time

def main():
    while True:
        func_input = input("기능 선택('크롤링/좋아요 누르기' 중 선택): ")
        if func_input.strip() == '크롤링':
            youtube_comment_crolling_v1.main()
            break
        elif func_input.strip() == '좋아요 누르기':
            ID_input = input('ID를 입력하세요!: ')
            PASS_input = input('PASS를 입력하세요!: ')
            youtube_comment_like_v2.main(ID_input, PASS_input)
            break
        else:
            print('잘못 입력하셨습니다!!')
            print('"크롤링" / "좋아요 누르기" 둘 중 하나를 정확히 입력해주세요!! ')
            continue

if __name__ == "__main__":
    main()
