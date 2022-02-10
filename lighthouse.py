from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()
driver.get("https://www.google.com/")