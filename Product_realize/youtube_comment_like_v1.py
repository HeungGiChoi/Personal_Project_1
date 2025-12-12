## 유튜브 댓글 좋아요 클릭 v1
## 함수화 / try-except 미적용
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("user-data-dir=C:\\Users\\choi heung ki\\Desktop\\ytlogin")
options.add_argument("disable-blink-features=AutomationControlled")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

input_url = input('URL을 입력하세요: ')
# test url : https://www.youtube.com/watch?v=gvELV_sUqpg
driver.get(input_url)
driver.maximize_window()
time.sleep(2)

# 구글 ID, password
yt_id = '01028298270'
yt_pass = 'gmdtm457*@&)'

# # 로그인 화면 들어가기
yt_login = driver.find_element(By.CSS_SELECTOR, "div[id='masthead-container'] #end ytd-button-renderer yt-button-shape")
yt_login.click()
time.sleep(2)

# ID 입력
yt_login_id = driver.find_element(By.CSS_SELECTOR, "div.Xb9hP input[type='email']")
yt_login_id.send_keys(yt_id)
yt_login_id.send_keys(Keys.ENTER)
time.sleep(5)

# password 입력
yt_login_pass = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
yt_login_pass.send_keys(yt_pass)
yt_login_pass.send_keys(Keys.ENTER)

# 유튜브 영상 화면 전환까지 기다림
driver.implicitly_wait(30)
change_ytd = driver.find_elements(By.CSS_SELECTOR, 'ytd-app')

prev_height = driver.execute_script('return document.documentElement.scrollHeight')
# 현재 웹 문서 body 객체 
scroll_body = driver.find_element(By.CSS_SELECTOR, 'body')

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
        
comment_like_button = driver.find_elements(By.CSS_SELECTOR, "ytd-toggle-button-renderer[id='like-button'] button")
time.sleep(1)
for comment_like in comment_like_button:
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", comment_like)
    driver.implicitly_wait(5)
    comment_like.click()

time.sleep(2)
driver.quit()
# # comment_like_button = driver.find_element(By.CSS_SELECTOR, "ytd-toggle-button-renderer[id='like-button'] yt-button-shape")