import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

NO_REKENING = ""
USERID = ""
PASSWD = ""
delay = 30
file_mutasi = "mutasi.txt"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("https://ibank.bankmandiri.co.id/retail3/")
browser.switch_to_frame("mainFrame")
el = browser.find_element_by_id("userid_sebenarnya")
el.send_keys(USERID)
el = browser.find_element_by_id("pwd_sebenarnya")
el.send_keys(PASSWD)
el = browser.find_element_by_id("btnSubmit")
el.click()
time.sleep(5)
#print("after login: " + browser.current_url)
# after login
el = browser.find_element_by_id("currentId-" + NO_REKENING)
el = el.find_element_by_tag_name("h3")
#print(el.text)
el.click()
time.sleep(5)
# download mutasi    
el = browser.find_element_by_id("globalTable")
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "history-list-name")))
    #print("Mutasi:\n" + el.text)
    f = open(file_mutasi,"w+")
    f.write(el.text);
    f.close();

except TimeoutException:
    print("Request timeout!")
    

browser.get("https://ibank.bankmandiri.co.id/retail3/loginfo/logout")
time.sleep(3)    
browser.quit()

