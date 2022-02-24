import pandas as pd
import pytest
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
df = pd.read_excel('Libro1.xlsx', sheet_name='Hoja1',  header=None)
class Test_BiogenesisDEV():
    def test_setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        self.driver.maximize_window()
        url = 'https://biogenesisdev.wpengine.com/'
        "definimos en una variable nuestra url"
        self.driver.get(url)
        for i in range(20):
            matriz_listas = df.loc[i].values.tolist()
            try:
                time.sleep(4)
                btn_ingresar = self.driver.find_element(By.LINK_TEXT, "Ingresar")
                btn_ingresar.click()
            except:
                time.sleep(4)
                btn_ingresar = self.driver.find_element(By.CSS_SELECTOR, ".menu-item-632")
                btn_ingresar.click()
            self.driver.implicitly_wait(10)
            campo_username = self.driver.find_element(By.ID, 'username')
            campo_password = self.driver.find_element(By.ID, 'password')
            campo_username.send_keys(matriz_listas)
            campo_password.send_keys('test')
            btn_login = self.driver.find_element(By.ID, 'js-login-submit-btn')
            # ahora con los campos llenos necesitamos logearnos, asi que hacemos referencia al boton de login
            btn_login.click()
            for y in range(2):
                try:
                    self.driver.implicitly_wait(8)
                    producto1 = self.driver.find_element(By.LINK_TEXT, "Ver Detalle")
                    producto1.click()
                except:
                    self.driver.implicitly_wait(8)
                    self.driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div[2]/div/div[5]/a').click()
                self.driver.implicitly_wait(8)
                self.driver.find_element(By.CSS_SELECTOR, ".single_add_to_cart_button").click()
                self.driver.implicitly_wait(8)
                self.driver.find_element(By.LINK_TEXT, "Confirmar Solicitud").click()
                self.driver.implicitly_wait(5)
                self.driver.execute_script("window.scrollTo(0,1633)")
                self.driver.implicitly_wait(5)
                self.driver.find_element(By.XPATH, "(//input[@id=\'\'])[2]").click()
                provinciaDropdown = Select(self.driver.find_element(By.NAME, "billing_distributor_province"))
                provinciaDropdown.select_by_visible_text("FORMOSA")
                self.driver.implicitly_wait(5)
                ciudadDropdown = Select(self.driver.find_element(By.NAME, "billing_distributor_locality"))
                ciudadDropdown.select_by_visible_text("FORMOSA")
                self.driver.implicitly_wait(5)
                veterinariaDropdown = Select(self.driver.find_element(By.NAME, "billing_distributor"))
                veterinariaDropdown.select_by_visible_text("BOVITEC FORMOSA")
                time.sleep(4)
                self.driver.find_element(By.ID, "place_order").click()
                time.sleep(4)
                self.driver.find_element(By.ID, "js-correct-details").click()
                self.driver.implicitly_wait(10)
                self.driver.find_element(By.ID, "js-keep-buying").click()
                print("La compra fue correcta")
                time.sleep(4)
                try:
                    self.driver.implicitly_wait(8)
                    producto1 = self.driver.find_element(By.LINK_TEXT, "Ver Detalle")
                    producto1.click()
                    self.driver.implicitly_wait(8)
                    seleccionar_cantidad = self.driver.find_element(By.XPATH, '//div/input')
                    seleccionar_cantidad.send_keys(1)
                    self.driver.find_element(By.CSS_SELECTOR, ".single_add_to_cart_button").click()
                    self.driver.implicitly_wait(8)
                    self.driver.find_element(By.LINK_TEXT, "Confirmar Solicitud").click()
                    self.driver.implicitly_wait(5)
                    self.driver.execute_script("window.scrollTo(0,1633)")
                    self.driver.implicitly_wait(5)
                    self.driver.find_element(By.XPATH, "(//input[@id=\'\'])[2]").click()
                    provinciaDropdown = Select(self.driver.find_element(By.NAME, "billing_distributor_province"))
                    provinciaDropdown.select_by_visible_text("BUENOS AIRES")
                    self.driver.implicitly_wait(5)
                    ciudadDropdown = Select(self.driver.find_element(By.NAME, "billing_distributor_locality"))
                    ciudadDropdown.select_by_visible_text("AZUL")
                    self.driver.implicitly_wait(5)
                    veterinariaDropdown = Select(self.driver.find_element(By.NAME, "billing_distributor"))
                    veterinariaDropdown.select_by_visible_text("AGROPECUARIA LA HUELLA")
                    time.sleep(4)
                    self.driver.find_element(By.ID, "place_order").click()
                    time.sleep(4)
                    self.driver.find_element(By.ID, "js-correct-details").click()
                    self.driver.implicitly_wait(10)
                    self.driver.find_element(By.ID, "js-keep-buying").click()
                    print("La compra fue correcta")
                    self.driver.find_element(By.LINK_TEXT, "Mi Perfil").click()
                    self.driver.implicitly_wait(10)
                    self.driver.find_element(By.LINK_TEXT, "Cerrar Sesión").click()
                    time.sleep(4)
                except:
                    self.driver.find_element(By.LINK_TEXT, "Mi Perfil").click()
                    self.driver.implicitly_wait(10)
                    self.driver.find_element(By.LINK_TEXT, "Cerrar Sesión").click()
                    time.sleep(4)
        self.driver.close()
