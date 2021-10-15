import pytest
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_setUp():
    "lo primero que tenemos que hacer es crear nuestra situacion initial"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    driver.maximize_window()
    #definimos que necesitamos iniciar el webdriver de chrome y le ponemos la direccion donde se encuentra
    url = 'https://biodevel:b8eda32d@biodevel.wpengine.com/'
    "definimos en una variable nuestra url"
    driver.get(url)
    #hay que leer esto como si fuera una historia por ejemplo self.driver.get(url), podemos decir que es
    #situacion inicial, en el driver, le damos la siguiente url
    #ahora vamos a logearnos
    driver.implicitly_wait(10)
    #implicity wait es un temporizador, pone en pausa por asi decirlo al webdriver hasta que encuentra la siguiente
    #linea, esto nos sirve para cuando cargamos una pag y necesitamos esperar cierto tiempo a que termine de cargar
    btn_ingresar = driver.find_element_by_id('menu-item-632')
    #creamos una variable que es un boton y le decimos donde encontrarlo.
    btn_ingresar.click()
    #a nuestro boton ingresar lo clickeamos
    driver.implicitly_wait(10)
    #volvemos a esperar
    campo_username = driver.find_element_by_id('username')
    print(campo_username.value_of_css_property('font-family'))
    campo_password = driver.find_element_by_id('password')
    print(campo_password.value_of_css_property('font-family'))
    #ahora creamos variables para hacer referencia a los campos de username y password
    campo_username.send_keys('tester052001@gmail.com')
    campo_password.send_keys('@DK@2iRbJhNNN&eMFRdus%KL')
    #a los campos username y password le enviamos las siguientes letras
    btn_login = driver.find_element_by_id('js-login-submit-btn')
    #ahora con los campos llenos necesitamos logearnos, asi que hacemos referencia al boton de login

    btn_login.click()
    #clickeamos el boton de login
"def test_bucle(self):"
    #self.test_login()
    #for i in range(20):
     #   self.driver.implicitly_wait(8)
      #  producto1 = self.driver.find_element_by_xpath(
      #      "//body/div[@id='page']/div[@id='content']/div[@id='primary']/main[@id='main']/section[2]/div[1]/div[2]/div[1]/div[5]/a[1]")
       # producto1.click()
        #self.driver.implicitly_wait(8)
        #seleccionar_cantidad = self.driver.find_element_by_xpath('//div/input')
        #seleccionar_cantidad.send_keys(1)
        #btn_agregarcarrito = self.driver.find_element_by_xpath(
        #    '/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/main[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[2]/div[3]/button[1]')
        #btn_agregarcarrito.click()
        #self.driver.implicitly_wait(5)
        #btn_agregarpedido = self.driver.find_element_by_xpath("//a[contains(text(),'Confirmar Solicitud')]")
        #btn_agregarpedido.click()

        #self.driver.implicitly_wait(5)
        #self.driver.execute_script("window.scrollTo(0,1633)")
        #self.driver.find_element(By.XPATH, "(//input[@id=\'\'])[2]").click()
        #self.driver.find_element(By.ID, "billing_distributor_province").click()
        #dropdown1 = self.driver.find_element(By.ID, "billing_distributor_province")
        #time.sleep(3)
        #dropdown1.find_element(By.XPATH, "//option[. = 'FORMOSA']").click()
        #time.sleep(4)
        #self.driver.find_element(By.ID, "billing_distributor_locality").click()
        #time.sleep(4)
        #dropdown2 = self.driver.find_element(By.ID, "billing_distributor_locality")
        #self.driver.implicitly_wait(4)
        #dropdown2.find_element(By.XPATH, "//option[. = 'FORMOSA']").click()
        #self.driver.find_element(By.XPATH, "//p[@id=\'billing_distributor_field\']/span/select").click()
        #self.driver.implicitly_wait(4)
        #dropdown3 = self.driver.find_element(By.ID, "billing_distributor")
        #self.driver.implicitly_wait(4)
        #dropdown3.find_element(By.XPATH, "//option[. = 'BOVITEC FORMOSA']").click()
        #self.assertTrue(dropdown3, msg="BOVITEC FORMOSA")
        #self.driver.implicitly_wait(5)
        #self.driver.find_element(By.ID, "place_order").click()
        #self.driver.implicitly_wait(5)
        #self.driver.find_element(By.ID, "js-keep-buying").click()
        #images = self.driver.find_elements_by_tag_name('img')
        #for img in images:
         #   dimensions = img.size
          #  width = dimensions['width']
           # height = dimensions['height']
            #print('{}x{}'.format(width, height))
        #print(i)"


