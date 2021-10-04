from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Посчитать сумму заданных чисел
    num_1 = browser.find_element_by_id('num1')
    x = num_1.text
    num_2 = browser.find_element_by_id('num2')
    y = num_2.text
    summ = int(x) + int(y)

    #Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))  # ищем элемент с текстом "Python"

    #Нажать кнопку "Submit"
    browser.find_element_by_class_name('btn-default').click()

finally:
    time.sleep(5)
    browser.quit()