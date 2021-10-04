from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://SunInJuly.github.io/execute_script.html'

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
    robot_check = browser.find_element_by_id('robotCheckbox')
    robot_check.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_id('robotsRule'))
    browser.find_element_by_id('robotsRule').click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_class_name('btn'))
    browser.find_element_by_class_name('btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()