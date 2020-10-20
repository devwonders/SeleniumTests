from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')

url = "localhost:8100"
name = "cart-outline"
action = "click"
domClass = "nothing"


#This example requires Selenium WebDriver 3.13 or newer
# with webdriver.Chrome() as driver:

 # .send_keys(keys + Keys.RETURN)
# first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
# print(first_result.get_attribute("textContent"))
# wait = WebDriverWait(driver, 10)
# driver.quit();
def main():
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    #driver.find_element(By.NAME, name).click()
    doElement(name, action)

def doElement(name, action):
    el = driver.find_element(By.NAME, name)
    switcher = {
        "click": el.Click()
    }
    switcher.get(action)

if __name__ == "--main--":
    main()
