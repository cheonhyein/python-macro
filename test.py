from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.set_window_size(1400, 1000)
# driver.get('https://www.aimingmarket.com/?idx=325')
driver.get('https://ticket.interpark.com/Gate/TPLogin.asp')
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('ID') # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'userPwd')
userPwd.send_keys('PASSWORD') # 로그인 할 계정의 패스워드
# userPwd.send_keys(Keys.ENTER)


while(True):
    pass


print("Test")