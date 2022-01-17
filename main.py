from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time 

INFO = '3644'
PRIORITY = ['timelabel02 timeBG20', 'timelabel01 timeBG20', 'timelabel02 timeBG19', 'timelabel01 timeBG19']

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
print("[완료] 로그인")

driver.implicitly_wait(0.2)


# 예약 화면 
red = driver.find_element_by_xpath('//div[@class="pay-button11"]')
red.click()
print("[진입] 예약화면")
driver.implicitly_wait(0.2)
driver.execute_script("window.scrollTo(0,2000)") 
# 8시에 풀림

execute = 0
count = 1

while(execute == 0):
    try:
        driver.find_element(By.XPATH, f'//div[@class="{PRIORITY[0]}"]/following-sibling::div').click()
        print(f"[진입] {PRIORITY[0].split('BG')[1]}시 {PRIORITY[0].split()[0].split('timelabel0')[1]}번째 수업 화면")

        while(execute == 0):
            try:
                driver.find_element_by_xpath('//div[@class="AVBtn"]').click()
                print("[완료] 예약")
                
                execute = 1


            except:
                driver.find_element_by_xpath('//div[@class="CloseBtn"]').click()
                time.sleep(0.1)

                driver.execute_script("window.scrollTo(0,2000)") 

                driver.find_element(By.XPATH, f'//div[@class="{PRIORITY[count]}"]/following-sibling::div').click()
                print(f"[진입] {PRIORITY[count].split('BG')[1]}시 {PRIORITY[count].split()[0].split('timelabel0')[1]}번째 수업 화면")
                count += 1    
                if(count == len(PRIORITY)): 
                    print("[불가] 예약 마감")
                    execute = 1
    except:
        print("[불가] 8시 이전")
        # driver.refresh()

        time.sleep(0.15)
# 
