import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

def mass_unfollow():
    # Detach Chrome Window, and not auto close when code finishes.
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 200)

    # Open Sign in page
    driver.get("https://www.linkedin.com/?trk=guest_homepage-basic_nav-header-logo/")
    wait = WebDriverWait(driver, 800)
    time.sleep(150)  # Time for user to login

    # Send login id & password
    # driver.find_element(By.ID, "session_key").send_keys("abc@gmail.com")
    # driver.find_element(By.ID, "session_password").send_keys("XXXX")
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # time.sleep(50)

    # Open New TAB
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')

    # Open the following page
    driver.get("https://www.linkedin.com/mynetwork/network-manager/people-follow/followers/")
    wait = WebDriverWait(driver, 800)

    # Scroll till bottom

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get all following buttons list
    wait = WebDriverWait(driver, 800)
    ele_list = driver.find_elements(By.XPATH, "//button[contains(.,'Following')]")

    # Pop the following tab element
    ele_list.pop(0)
    l = len(ele_list)

    print(f"Number of connections following : {l}")

    i = 1  # Count for number for folks unfollowed
    for ele in ele_list:
        # Scroll to the element in focus
        wait = WebDriverWait(driver, 800)
        print(str(i) + '. ' + ele.get_attribute("aria-label"))  # Unfollowed person details
        i += 1
        iframe = driver.find_element(By.ID, ele.get_attribute("id"))
        ActionChains(driver).scroll_to_element(iframe).perform()
        time.sleep(1)
        # Click on following button
        t1_button = driver.find_element(By.ID, ele.get_attribute("id"))
        driver.execute_script("arguments[0].click();", t1_button)
        time.sleep(1)
        # Click on unfollow button
        wait = WebDriverWait(driver, 1000)
        button = driver.find_element(By.XPATH, "//button[contains(.,'Unfollow')]")
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)

    print(f"Number of connections unfollowed : {i}")




if __name__ == '__main__':
   mass_unfollow()