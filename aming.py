import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys



def clickCount() :
    while True:
        try:
            selectboxoption = driver.find_element(By.XPATH, '//*[@id="prod_options"]/div/div/div[2]').click()
            print("click시도")
        except:
            print("error")
        else:
            print("에러없음!")
            break





options = webdriver.ChromeOptions()
# // 페이지 로딩에서 이미지 제외
options.add_argument("--blink-settings=imagesEnabled=false")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_window_size(1400, 1000)
driver.get('https://www.aimingmarket.com/?idx=337')
# driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.NAME, 'uid')
userId.send_keys('GPDLS2574')
# 로그인 할 계정 id
userPwd = driver.find_element(By.NAME, 'passwd')
userPwd.send_keys('wxum1570')
# 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)

driver.implicitly_wait(10)


#
# while True:
#     minute = datetime.now().minute
#     time.sleep(0.1)
#     if minute == 00 or minute == 0:
#         print("00초!!")
#         driver.refresh()
#         break
#     else:
#         print(minute)
#
#
# time.sleep(0.1)
#
# while True:
#     soldOut = driver.find_element(By.XPATH, '//*[@id="prod_goods_form"]/div[10]/div/div')
#     if not soldOut:
#         break
#     else:
#         if soldOut.text == '이 상품은 현재 판매기간이 아닙니다.':
#             driver.refresh()
#             time.sleep(0.05)
#         else:
#             break

# TODO test 중
clickCount()







print("try-except 탈출")

# selectbox = driver.find_element(By.XPATH, '//*[@id="prod_options"]/div/div/div[2]').click()
# time.sleep(0.1)
# selectboxoption = driver.find_element(By.XPATH, '//*[@id="prod_options"]/div/div/div[2]/div/div[4]/a').click()
# time.sleep(0.1)
# selectbox = driver.find_element(By.XPATH, '//*[@id="prod_options"]/div/div/div[2]').click()
# time.sleep(0.1)
# select1boxoption = driver.find_element(By.XPATH, '//*[@id="prod_options"]/div/div/div[2]/div/div[1]/a').click()
# time.sleep(0.1)
# selectbox = driver.find_element(By.XPATH, '//*[@id="prod_options"]/div/div/div[2]').click()
# time.sleep(0.1)
# select2boxoption = driver.find_element(By.XPATH, '//*[@id="prod_options"]/div/div/div[2]/div/div[5]/a').click()


sample = driver.find_element(By.XPATH, '//*[@id="prod_options"]/div/div/div[2]')

time.sleep(0.1)
# select2boxoption = driver.find_element(By.XPATH, '//*[@id="prod_goods_form"]/div[8]/a[1]').click()

# //*[@id="prdOption0"]/div/div[2]/div[1]/div/a[2]   -> 플러스 버튼 누르기

while(True):
    pass


print("Test")