import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(15)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(15)

# От меня дополнение в качестве регистрации на сайте
reg = driver.find_element_by_link_text("Войти")
reg.click()
time.sleep(5)
text_email = driver.find_element_by_name("login")
text_email.send_keys("man@a-real.ru")
text_pswd = driver.find_element_by_name("password")
text_pswd.send_keys("123stepik")
time.sleep(5)
enter_reg = driver.find_element_by_css_selector(".sign-form__btn")
enter_reg.click()
time.sleep(10)


# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")
#textarea2 = driver2.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
#textarea2.send_keys("get()")
time.sleep(15)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")
#submit_button2 = driver2.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
# Если закрыть браузер по крестику, процесс будет висеть в оперативе
driver.quit()