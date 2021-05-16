#базовая страница, от которой будут унаследованы все остальные классы. В ней описываются вспомогательные методы для работы с драйвером.

#from .locators import BaseLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage():  #конструктор класса
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): #открытие нужной страницы в браузере
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


