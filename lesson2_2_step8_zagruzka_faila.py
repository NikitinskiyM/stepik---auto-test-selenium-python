import os
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Заполнить текстовые поля: имя, фамилия, email
    browser.find_element_by_name('firstname').send_keys('Mikhail')
    browser.find_element_by_name('lastname').send_keys('Niki')
    browser.find_element_by_name('email').send_keys('a@a.ru')

    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    browser.find_element_by_id('file').send_keys(file_path)

    #Нажать кнопку "Submit"
    browser.find_element_by_class_name('btn').click()
finally:
    time.sleep(10)
    browser.quit()