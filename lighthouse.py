from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://googlechrome.github.io/lighthouse/viewer/")
enviar_archivo = driver.find_element_by_link_text("https://googlechrome.github.io/lighthouse/viewer/")
enviar_archivo.send_keys("C:/Users/ericl/PycharmProjects/TemplateSelenium/report.json")