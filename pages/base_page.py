class BasePage():
    def __init__(self, browser,url):
        #добавим конструктор — метод, который вызывается, когда мы создаем объект
        #качестве параметров мы передаем экземпляр драйвера и url адрес
        self.browser = browser
        self.url = url

    def open(self):
        #должен открывать нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)

