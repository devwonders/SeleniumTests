from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)

driver.get("localhost:8100")
# print(driver.title)
search = driver.find_elements_by_class_name("title");
print(search.values)
driver.close()
driver.quit()
