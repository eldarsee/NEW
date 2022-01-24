from selenium import webdriver
import time 
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_el = browser.find_element_by_id("treasure")
    x = x_el.get_attribute("valuex")
    INPUT  = browser.find_element_by_id("answer") 
    INPUT.send_keys(calc(x))
    browser.find_element_by_xpath("//*[@id='robotCheckbox']").click()
    browser.find_element_by_xpath("//*[@value='robots']").click()
    browser.find_element_by_xpath("//*[@type='submit']").click()
finally:
    time.sleep(5)
    browser.quit()
