from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(1400, 1000)
driver.get('https://www.aimingmarket.com/?idx=334')
# driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.NAME, 'uid')
userId.send_keys('GPDLS2574')
# 로그인 할 계정 id
userPwd = driver.find_element(By.NAME, 'passwd')
userPwd.send_keys('wxum1570')
# 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
soldOut = driver.find_element(By.XPATH, '//*[@id="prod_goods_form"]/div[8]/a[1]/span')
print(soldOut.text)

while True:
    if soldOut.text == '품절된 상품입니다.':
        driver.refresh()
        driver.implicitly_wait(10)
    else:
        break;

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="prod_goods_form"]/div[8]/a[1]/span'))
#     )
#
# finally:
#     driver.quit()




while(True):
    pass


print("Test")