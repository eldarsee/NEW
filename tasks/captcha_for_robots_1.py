from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_el = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_el.text
    y = calc(x)   
    INPUT  = browser.find_element_by_class_name("form-control") 
    time.sleep(2)
    INPUT.send_keys(y)
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='robotCheckbox']").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[@value='robots']").click()
    browser.find_element_by_xpath("//*[@type='submit']").click()
finally:
    time.sleep(3)
    browser.quit()
