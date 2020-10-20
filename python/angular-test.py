from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# define a class Addition
class Browse:

    # define a constructor
    def __init__(self):
        self.options = webdriver.ChromeOptions() 
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=self.options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')      
        self.defaultWait = 10;
    
    # define a constructor
    #def __init__(self, num1, num2):
    #    self.num1 = num1
    #    self.num2 = num2
            
    # define an instance method to add
    #def add(self):
    #    return self.num1+ self.num2
    def getDriver(self):
        return self.driver

    def doElement(self,name,action):
        el = self.driver.find_element(By.NAME, name)
        print(el)
        switcher = {
            "click": el.click()
        }
        switcher.get(action)
    
    def nav(self,url,waitTime):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, waitTime)
        print(wait)
    
    def waitFor(self,waitTime):
        wait = WebDriverWait(self.driver, waitTime = self.defaultWait)

def main():
    url = "localhost:8100"
    name = "cart-outline"
    action = "click"
    waitTime = 10
    domClass = "nothing"  
    browser = Browse()
    # driver = browser.getDriver()
    browser.nav(url,waitTime)
    browser.doElement(name,action)
    browser.wait()

main()
