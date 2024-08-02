from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=chrome_options)
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
chrome_browser.implicitly_wait(2)
search = chrome_browser.find_element(By.ID, 'user-message')
search.send_keys('Hello world!!!')
btn = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
chrome_browser.implicitly_wait(2)
btn.click() 
op_message = search.get_attribute('value')
print(op_message)


# while True:
#     choice = str(input("Enter 'Y' to exit:\n"))
#     if choice in ('y', 'Y'):
#         break
# chrome_browser.close()
