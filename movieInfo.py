from selenium import webdriver
import time

br = webdriver.Chrome('C:/chromedriver.exe')
br.implicitly_wait(15) # wait's for the page to get done loading before it does anything with it
br.get('http://www.google.com/')
# to fill out a form
search = br.find_element_by_name('q')
search.send_keys('blade runner')
search.submit()
time.sleep(5)
print(br.title)

quit()