import unittest
from selenium import webdriver

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        url = 'https://develop-plastic-ingenuity.pantheonsite.io/capabilities-services/'
        self.driver.get(url)

    def testTipgrafia(self):
        self.driver.implicitly_wait(10)
        title_modulebasic = self.driver.find_element_by_xpath("//div[contains(text(),'A Full Package of Benefits')]")
        titlefont_family = "Rubik, sans-serif"
        titlefont_size = "40px"
        titleline_height = "47px"
        title_letter_spacing = "-1px"
        if titlefont_family != title_modulebasic.value_of_css_property('font-family'):
            print("Son distintos los font family title")
            print(title_modulebasic.value_of_css_property('font-family'))
            title_modulebasic.screenshot("title.png")
        if titlefont_size != title_modulebasic.value_of_css_property('font-size'):
            print("Son distintos los font size del title")
            print(title_modulebasic.value_of_css_property('font-size'))
            title_modulebasic.screenshot("title.png")
        if titleline_height != title_modulebasic.value_of_css_property('line-height'):
            print("Son distintos del title")
            print(title_modulebasic.value_of_css_property('line-height'))
            title_modulebasic.screenshot("title.png")
        if title_letter_spacing != title_modulebasic.value_of_css_property('letter-spacing'):
            print("Es distinto el letter spacing del title")
            print(title_modulebasic.value_of_css_property('letter-spacing'))
            title_modulebasic.screenshot("title.png")
        text_modulebasic = self.driver.find_element_by_xpath(
            "//p[contains(text(),'Our unique set of capabilities and services allows')]")
        textbasic_family = "Mulish, sans-serif"
        textfont_size = "16px"
        textline_height = "24px"
        text_letter_spacing = "normal"
        if textbasic_family != text_modulebasic.value_of_css_property('font-family'):
            print("Son distinctions los font family text subtitle")
            print(text_modulebasic.value_of_css_property('font-family'))
            text_modulebasic.screenshot("text_modulobasic.png")
        if textfont_size != text_modulebasic.value_of_css_property('font-size'):
            print("Son distinctions los sizes text subtitle")
            print(text_modulebasic.value_of_css_property('font-size'))
            text_modulebasic.screenshot("text_modulobasic.png")
        if textline_height != text_modulebasic.value_of_css_property('line-height'):
            print("Son distinctions los line height de text subtitle")
            print(text_modulebasic.value_of_css_property('line-height'))
            text_modulebasic.screenshot("text_modulobasic.png")
        if text_letter_spacing != text_modulebasic.value_of_css_property('letter-spacing'):
            print("Son distinctions los letter spacing del text subtitle")
            print(text_modulebasic.value_of_css_property('letter-spacing'))
            text_modulebasic.screenshot("text_modulobasic.png")

        subtitle_text = self.driver.find_element_by_xpath("//div[contains(text(),'Test & Scale')]")
        subtitle_text_family = "Rubik, sans-serif"
        subtitle_size = "21px"
        subtitle_height = "28px"
        subtitle_letter_spacing = "normal"
        if subtitle_text_family != subtitle_text.value_of_css_property('font-family'):
            print("Son distintos los font family del subtitle")
            print(subtitle_text.value_of_css_property('font-family'))
            subtitle_text.screenshot("subtitle_text.png")
        if subtitle_size != subtitle_text.value_of_css_property('font-size'):
            print("Son distintos los sizes del subtitle")
            print(subtitle_text.value_of_css_property('font-size'))
            subtitle_text.screenshot("subtitle_text.png")
        if subtitle_height != subtitle_text.value_of_css_property('line-height'):
            print("Son distintos los line height del subtitle")
            print(subtitle_text.value_of_css_property('line-height'))
            subtitle_text.screenshot("subtitle_text.png")
        if subtitle_letter_spacing != subtitle_text.value_of_css_property('letter-spacing'):
            print("Son distintos los letter spacing del subtitle")
            print(subtitle_text.value_of_css_property('letter-spacing'))
            subtitle_text.screenshot("subtitle_text.png")