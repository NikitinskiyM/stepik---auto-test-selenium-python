from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Ищем элемент-картинку, который является изображением сундука с сокровищами
    #Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    #Посчитать математическую функцию от x (сама функция остаётся неизменной).
    x_element = browser.find_element_by_tag_name('img')
    x_checked = x_element.get_attribute('valuex')
    y = calc(x_checked)

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