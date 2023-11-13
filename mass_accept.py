import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


#Detach Chrome Window, and not auto close when code finishes.
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 200)

#Open Sign in page
driver.get("https://www.linkedin.com/?trk=guest_homepage-basic_nav-header-logo/")
wait = WebDriverWait(driver, 800)
time.sleep(50) #Time for user to login

# Send login id & password
# driver.find_element(By.ID, "session_key").send_keys("abc@gmail.com")
# driver.find_element(By.ID, "session_password").send_keys("XXXX")
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# time.sleep(50)




i=0 #Page count
j=0 #Total Accepted request count
while i<25: #Number of pages = Number of request / 100
#Open the following page
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
    driver.get("https://www.linkedin.com/mynetwork/invitation-manager/?filterCriteria=&invitationType=&page=1")
    wait = WebDriverWait(driver, 800)
    i+=1
    time.sleep(5)

    #Get all accept buttons list
    wait = WebDriverWait(driver, 800)
    ele_list = driver.find_elements(By.XPATH,"//button[contains(.,'Accept')]")

    for ele in ele_list:
        #Scroll to the element in focus
        wait = WebDriverWait(driver, 800)
        j+=1
        iframe = driver.find_element(By.ID, ele.get_attribute("id"))
        ActionChains(driver).scroll_to_element(iframe).perform()
        time.sleep(1)
        #Click on accept button
        t1_button = driver.find_element(By.ID, ele.get_attribute("id"))
        driver.execute_script("arguments[0].click();", t1_button)
        time.sleep(1)

    print(f"Number of connections accepted till now: {j}")