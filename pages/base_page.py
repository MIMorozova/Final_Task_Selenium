#базовая страница, от которой будут унаследованы все остальные классы. В ней описываются вспомогательные методы для работы с драйвером.


class BasePage():  #конструктор класса
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): #открытие нужной страницы в браузере
        self.browser.get(self.url)


