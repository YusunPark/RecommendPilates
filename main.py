from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time 

INFO = '3644'
PRIORITY = ['timelabel02 timeBG18']

# 로그인 화면 팝업
URL = "https://dagympilates36.flexgym.biz/mobile/" 

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)


# 로그인
ID = driver.find_element_by_xpath('//input[@name="memberID"]')
ID.send_keys(INFO)

PW = driver.find_element_by_xpath('//input[@name="memberPW"]')
PW.send_keys(INFO)
PW.send_keys(Keys.RETURN)
print("[로그인] 완료")

driver.implicitly_wait(0.2)


# 예약 화면 
red = driver.find_element_by_xpath('//div[@class="pay-button11"]')
red.click()
print("[예약화면] 진입")
driver.implicitly_wait(0.2)

# 8시에 풀림

execute = 0
while(execute == 0):
    try:
        driver.find_element(By.XPATH, f'//div[@class="{PRIORITY[0]}"]/following-sibling::div').click()
        execute = 1
        print(f"{PRIORITY[0].split('BG')[1]}시 {PRIORITY[0].split()[0].split('timelabel0')[1]}번째 수업시간 선택")

    except:
        print("아직 시간이 아님")
        time.sleep(0.15)


driver.find_element_by_xpath('//div[@class="AVBtn"]').click()
print("예약 완료")