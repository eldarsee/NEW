from selenium import webdriver
import time 

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome('D:/Пайтон/ChromeDriver')
    browser.get(link)
    element = browser.find_element_by_tag_name("input")
    element.send_keys("Jakov")
    element = browser.find_element_by_xpath("//*[@placeholder='Input your last name']")
    element.send_keys("Fak")
    element = browser.find_element_by_xpath("//*[@placeholder='Input your email']")
    element.send_keys("my email")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()
