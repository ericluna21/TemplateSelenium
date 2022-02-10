import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
class Test_imago_pageHow():
    def test_Imago_who_we_are(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        self.driver.maximize_window()
        print("Inicio del test")
        self.driver.get('https://imagoggdev:!wcanvas2021!@imagoggdev.wpengine.com/who-we-are/')
        self.driver.implicitly_wait(10)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        Mission_VisionModule_Title = self.driver.find_element_by_xpath("//p[contains(text(),'We Help')]")
        assert Mission_VisionModule_Title.screenshot("Mission_VisionTitle.png")
        Mission_VisionModule_CopyTitle = self.driver.find_element_by_xpath("//div[contains(text(),'Our Mission')]")
        assert Mission_VisionModule_CopyTitle.screenshot("Mission_VisionTitleCopy.png")

    def test_Imago_Numbers(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('https://imagoggdev:!wcanvas2021!@imagoggdev.wpengine.com/who-we-are/')
        numbertitle = self.driver.find_element_by_xpath("//strong[contains(text(),'Our Impact in Numbers')]")
        assert numbertitle.screenshot("NumberTitle.png")
        print("Se encontro el texto")
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        self.driver.implicitly_wait(10)
        numbers_firth = self.driver.find_element_by_xpath("//div[contains(text(),'113')]")
        assert  numbers_firth.screenshot("NumberFirths.png")
