# 메인 프로그램
import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

try:
    # 최신 ChromeDriver 설치 및 사용
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
except Exception as e:
    print("XX 웹 드라이버 초기화 또는 설치에 실패했습니다.")
    print(f"오류: {e}")
    sys.exit(1)

try:
    driver.get("https://www.youtube.com/watch?v=LZP-Gk1B7x8")
except Exception as e:
    print(f"URL 접속 불가!!: {e}")
    driver.quit()
else:
    driver.maximize_window()
    time.sleep(2)

# 맨 밑까지 스크롤
# 과거 웹 문서 높이 객체 
prev_height = driver.execute_script('return document.documentElement.scrollHeight')
# 현재 웹 문서 body 객체 
scroll_body = driver.find_element(By.CSS_SELECTOR, 'body')

# PAGE_DOWN으로 스크롤
# 여러번 해야 동적 페이지 업데이트 됨
while True:
    scroll_body.send_keys(Keys.PAGE_DOWN)
    scroll_body.send_keys(Keys.PAGE_DOWN)
    scroll_body.send_keys(Keys.PAGE_DOWN)
    scroll_body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    # 스크롤 후 현재 웹 문서 높이 객체
    current_height = driver.execute_script('return document.documentElement.scrollHeight')

    # 현재와 과거 웹 문서 높이 비교
    # 같으면 맨 밑 댓글 도달로 파악하고 탈출
    if current_height == prev_height:
        time.sleep(1)
        break
    else:
        prev_height = current_height

# 댓글 요소들 저장 함수
try:
    # 댓글 작성자 리스트 
    author = driver.find_elements(By.CSS_SELECTOR, 'div.style-scope.ytd-comment-view-model h3.style-scope.ytd-comment-view-model a.yt-simple-endpoint.style-scope.ytd-comment-view-model span.style-scope.ytd-comment-view-model.style-scope.ytd-comment-view-model')
    author_text = [i.text for i in author]
except Exception as e:
    print(f'댓글 요소 크롤링 중 오류 발생: {e}')

try:
    # 댓글 작성 시간 리스트
    required_time = driver.find_elements(By.CSS_SELECTOR, 'div.style-scope.ytd-comment-view-model span.style-scope.ytd-comment-view-model a.yt-simple-endpoint.style-scope.ytd-comment-view-model')
    required_time_text = [i.text for i in required_time]
except Exception as e:
    print(f'댓글 요소 크롤링 중 오류 발생: {e}')

try:
    # 댓글 내용 리스트
    comment = driver.find_elements(By.CSS_SELECTOR, 'div.style-scope.ytd-expander yt-attributed-string.style-scope.ytd-comment-view-model span.yt-core-attributed-string.yt-core-attributed-string--white-space-pre-wrap')
    comment_text = [i.text for i in comment]
except Exception as e:
    print(f'댓글 요소 크롤링 중 오류 발생: {e}')

try:
    # 댓글 좋아요 수 리스트
    comment_like = driver.find_elements(By.CSS_SELECTOR, 'span.style-scope.ytd-comment-engagement-bar')
    comment_like_text = []
    # 댓글 좋아요가 숫자라면 그대로 리스트에 추가
    # 비어있다면 좋아요가 0개로 처리하고 추가
    for i in comment_like:
        try:
            if i.text.isdigit():
                comment_like_text.append(i.text)
            else:
                i = 0
                comment_like_text.append(i)
        except Exception as e:
            print(f'댓글 좋아요 수 변경 중 오류 발생: {e}')
except Exception as e:
    print(f'댓글 요소 크롤링 중 오류 발생: {e}')

# 최종 데이터 DataFrame 변수로 저장
total_data = pd.DataFrame({
    '댓글 작성자 ID': author_text,
    '댓글 내용': comment_text,
    '댓글 좋아요 수': comment_like_text,
    '작성 시간': required_time_text
})

try:
    # CSV 파일로 저장
    total_data.to_csv("C:\\Users\\choi heung ki\\Desktop\\댓글모음.csv")
    print("CSV 파일 저장 완료!")
except Exception as e:
    print(f'파일 저장 중 오류 발생: {e}')

driver.quit()