from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Считать значение для переменной x
    #Посчитать математическую функцию от x
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    #Ввести ответ в текстовое поле.
    browser.find_element_by_id('answer').send_keys(y)

    #Отметить checkbox "I'm the robot".
    #Выбрать radiobutton "Robots rule!".
    #Нажать на кнопку Submit.
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn-default').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()