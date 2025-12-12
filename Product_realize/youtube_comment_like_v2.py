## 유튜브 댓글 좋아요 클릭
## 함수화 / try-except 적용
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# # ID, PASS 입력받기
# # main 프로그램일때만 실행
# input_ID = input('ID를 입력하세요: ')
# input_PASS = input('PASS를 입력하세요: ')

# url로 웹 페이지 열기
def open_url(driver, url):
    try:
        driver.get(url)
    except Exception as e:
        print(f"URL 접속 불가!!: {e}")
        driver.quit()
    else:
        driver.maximize_window()
        time.sleep(2)

# 맨 밑까지 스크롤
def unlimit_scrolling(driver):
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

# 로그인
def login(driver, ID, PASS):
    try:
        # 로그인 화면 들어가기
        yt_login = driver.find_element(By.CSS_SELECTOR, "div[id='masthead-container'] #end ytd-button-renderer yt-button-shape")
        yt_login.click()
        time.sleep(2)
    except Exception as e:
        print(f'element를 찾는 중 오류가 발생했습니다: {e}')
    except (ElementClickInterceptedException, ElementNotInteractableException) as e:
        print(f'요소를 클릭하지 못했습니다: {e}')

    try:
        # ID 입력
        yt_login_id = driver.find_element(By.CSS_SELECTOR, "div.Xb9hP input[type='email']")
        yt_login_id.send_keys(ID)
        yt_login_id.send_keys(Keys.ENTER)
        time.sleep(5)
    except Exception as e:
        print(f'element를 찾는 중 오류가 발생했습니다: {e}')
    except (ElementClickInterceptedException, ElementNotInteractableException) as e:
        print(f'요소를 클릭하지 못했습니다: {e}')

    try:
        # password 입력
        yt_login_pass = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        yt_login_pass.send_keys(PASS)
        yt_login_pass.send_keys(Keys.ENTER)
    except Exception as e:
        print(f'element를 찾는 중 오류가 발생했습니다: {e}')
    except (ElementClickInterceptedException, ElementNotInteractableException) as e:
        print(f'요소를 클릭하지 못했습니다: {e}')
    
    # 유튜브 영상 화면 전환까지 기다림
    driver.implicitly_wait(30)
    change_ytd = driver.find_elements(By.CSS_SELECTOR, 'ytd-app')

# 댓글 좋아요 누르기
def comment_like_click(driver):
    comment_like_button = driver.find_elements(By.CSS_SELECTOR, "ytd-toggle-button-renderer[id='like-button'] button")
    time.sleep(1)

    # 각 댓글 좋아요 버튼 순회
    for comment_like in comment_like_button:
        try:
            # 각 댓글 좋아요 element가 화면 중앙에 오도록 자바 스크립트 활용
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", comment_like)
            driver.implicitly_wait(5)
            comment_like.click()
        except Exception as e:
            print(f'element를 찾는 중 오류가 발생했습니다: {e}')
        except (ElementClickInterceptedException, ElementNotInteractableException) as e:
            print(f'요소를 클릭하지 못했습니다: {e}')
    
    time.sleep(1)
    print('좋아요 댓글 누르기 작업을 완료했습니다!')
    
# 메인함수
def main(login_ID, login_pass):
    try:
        options = Options()
        # options.add_argument("user-data-dir=C:\\Users\\choi heung ki\\Desktop\\ytlogin")
        options.add_argument("disable-blink-features=AutomationControlled")
        # 최신 ChromeDriver 설치 및 사용
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print("XX 웹 드라이버 초기화 또는 설치에 실패했습니다.")
        print(f"오류: {e}")
        sys.exit(1)

    input_url = input('URL을 입력하세요: ')
    # https://www.youtube.com/watch?v=LZP-Gk1B7x8
    open_url(driver, input_url)
    time.sleep(1)

    login(driver, login_ID, login_pass)
    time.sleep(1)
    
    unlimit_scrolling(driver)
    time.sleep(1)

    comment_like_click(driver)
    time.sleep(1)

    driver.quit()
    
# 실행하는 모듈이 import 되지 않고 본 모듈이라면
if __name__ == "__main__":
    main(input_ID, input_PASS)
