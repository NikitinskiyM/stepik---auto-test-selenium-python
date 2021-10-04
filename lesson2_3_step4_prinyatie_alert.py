from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажать на кнопку
    browser.find_element_by_class_name('btn-primary').click()

    #Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    #Считать значение для переменной x
    #Посчитать математическую функцию от x
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле.
    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()