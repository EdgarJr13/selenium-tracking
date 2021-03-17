from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class CorreiosBot:
    def __init__(self, rastreio):
        self.rastreio = rastreio
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    def rastrear(self):
        driver = self.driver
        driver.get('https://www.correios.com.br')

        rastreioElement = driver.find_element_by_xpath('//*[@id="objetos"]')
        rastreioElement.send_keys(self.rastreio)
        time.sleep(2)
        rastreioElement.send_keys(Keys.RETURN)

"""rastreio = input('Digite o código de rastreio: ')

codigo = CorreiosBot(rastreio)

codigo.rastrear()

print(' ~~~ PROTUDO RASTREADO!! ;) ~~~')"""