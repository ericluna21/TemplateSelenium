import unittest
from selenium import webdriver

class Login(unittest.TestCase):
    def setUp(self):
        "lo primero que tenemos que hacer es crear nuestra situacion initial"
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        #definimos que necesitamos iniciar el webdriver de chrome y le ponemos la direccion donde se encuentra
        url = 'https://biodevel:b8eda32d@biodevel.wpengine.com/'
        "definimos en una variable nuestra url"
        self.driver.get(url)
        #hay que leer esto como si fuera una historia por ejemplo self.driver.get(url), podemos decir que es
        #situacion inicial, en el driver, le damos la siguiente url
    def test_login(self):
        #ahora vamos a logearnos
        self.driver.implicitly_wait(10)
        #implicity wait es un temporizador, pone en pausa por asi decirlo al webdriver hasta que encuentra la siguiente
        #linea, esto nos sirve para cuando cargamos una pag y necesitamos esperar cierto tiempo a que termine de cargar
        btn_ingresar = self.driver.find_element_by_id('menu-item-632')
        #creamos una variable que es un boton y le decimos donde encontrarlo.
        btn_ingresar.click()
        #a nuestro boton ingresar lo clickeamos
        self.driver.implicitly_wait(10)
        #volvemos a esperar
        campo_username = self.driver.find_element_by_id('username')
        campo_password = self.driver.find_element_by_id('password')
        #ahora creamos variables para hacer referencia a los campos de username y password
        campo_username.send_keys('tester052001@gmail.com')
        campo_password.send_keys('@DK@2iRbJhNNN&eMFRdus%KL')
        #a los campos username y password le enviamos las siguientes letras
        btn_login = self.driver.find_element_by_id('js-login-submit-btn')
        #ahora con los campos llenos necesitamos logearnos, asi que hacemos referencia al boton de login
        btn_login.click()
        #clickeamos el boton de login