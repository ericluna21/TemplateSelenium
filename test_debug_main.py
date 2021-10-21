import pytest
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
class Test_Biogenesis():
    def teardown_method(self, method):
        self.driver.quit()
    def setup_method(self, method):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        self.driver.maximize_window()
        url = 'https://biodevel:b8eda32d@biodevel.wpengine.com/'
        "definimos en una variable nuestra url"
        self.driver.get(url)
    def test_setUp(self):
        btn_ingresar = self.driver.find_element_by_id('menu-item-632')
        # creamos una variable que es un boton y le decimos donde encontrarlo.
        btn_ingresar.click()
        # a nuestro boton ingresar lo clickeamos
        self.driver.implicitly_wait(10)
        # volvemos a esperar
        campo_username = self.driver.find_element_by_id('username')
        campo_password = self.driver.find_element_by_id('password')
        # ahora creamos variables para hacer referencia a los campos de username y password
        campo_username.send_keys('tester052001@gmail.com')
        campo_password.send_keys('@DK@2iRbJhNNN&eMFRdus%KL')
        # a los campos username y password le enviamos las siguientes letras
        btn_login = self.driver.find_element_by_id('js-login-submit-btn')
        # ahora con los campos llenos necesitamos logearnos, asi que hacemos referencia al boton de login

        btn_login.click()
        for i in range (20):
            self.driver.implicitly_wait(8)
            producto1 = self.driver.find_element_by_xpath(
            "//body/div[@id='page']/div[@id='content']/div[@id='primary']/main[@id='main']/section[2]/div[1]/div[2]/div[1]/div[5]/a[1]")
            producto1.click()
            self.driver.implicitly_wait(8)
            seleccionar_cantidad = self.driver.find_element_by_xpath('//div/input')
            seleccionar_cantidad.send_keys(1)
            btn_agregarcarrito = self.driver.find_element_by_xpath(
            '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/main[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[2]/div[3]/button[1]')
            btn_agregarcarrito.click()
            self.driver.implicitly_wait(5)
            btn_agregarpedido = self.driver.find_element_by_xpath("//a[contains(text(),'Confirmar Solicitud')]")
            btn_agregarpedido.click()

            self.driver.implicitly_wait(5)
            self.driver.execute_script("window.scrollTo(0,1633)")
            self.driver.find_element(By.XPATH, "(//input[@id=\'\'])[2]").click()
            provinciaDropdown = Select(self.driver.find_element_by_name("billing_distributor_province"))
            provinciaDropdown.select_by_visible_text("FORMOSA")
            self.driver.implicitly_wait(5)
            ciudadDropdown = Select(self.driver.find_element_by_name("billing_distributor_locality"))
            ciudadDropdown.select_by_visible_text("FORMOSA")
            self.driver.implicitly_wait(5)
            veterinariaDropdown = Select(self.driver.find_element_by_name("billing_distributor"))
            veterinariaDropdown.select_by_visible_text("BOVITEC FORMOSA")
            time.sleep(4)
            self.driver.find_element(By.ID, "place_order").click()
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.ID, "js-keep-buying").click()
            print(i)
        self.driver.close()