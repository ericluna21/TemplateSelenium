import unittest
from selenium import webdriver

class Tipografia(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        url = 'https://develop-plastic-ingenuity.pantheonsite.io/capabilities-services/'
        self.driver.get(url)

    def test_tipoHero(self):
        self.driver.implicitly_wait(10)
        hero_title = self.driver.find_elements_by_id()
        hero_title_fontfamily = "Campaign, sans-serif"
        hero_title_fontsize = "55px"
        hero_title_lineheight = "60px"
        hero_title_spaceletter = "normal"
        if hero_title_fontfamily != hero_title.value_of_css_property('font-family'):
            print("Son distintos los font family title")
            print(hero_title.value_of_css_property('font-family'))
            hero_title.screenshot("title.png")
        if hero_title_fontsize != hero_title.value_of_css_property('font-size'):
            print("Son distintos los font size del title")
            print(hero_title.value_of_css_property('font-size'))
            hero_title.screenshot("title.png")
        if hero_title_lineheight != hero_title.value_of_css_property('line-height'):
            print("Son distintos del title")
            print(hero_title.value_of_css_property('line-height'))
            hero_title.screenshot("title.png")
        if hero_title_spaceletter != hero_title.value_of_css_property('letter-spacing'):
            print("Es distinto el letter spacing del title")
            print(hero_title.value_of_css_property('letter-spacing'))
            hero_title.screenshot("title.png")

        hero_subtitle = self.driver.find_elements_by_id()
        hero_subtitle_fontfamily = "Campaign, sans-serif"
        hero_subtitle_fontsize = "20px"
        hero_subtitle_lineheight = "22px"
        hero_subtitle_spaceletter = "normal"
        if hero_subtitle_fontfamily != hero_subtitle.value_of_css_property('font-family'):
            print("Son distintos los font family title")
            print(hero_subtitle.value_of_css_property('font-family'))
            hero_subtitle.screenshot("title.png")
        if hero_subtitle_fontsize != hero_subtitle.value_of_css_property('font-size'):
            print("Son distintos los font size del title")
            print(hero_subtitle.value_of_css_property('font-size'))
            hero_subtitle.screenshot("title.png")
        if hero_subtitle_lineheight != hero_subtitle.value_of_css_property('line-height'):
            print("Son distintos del title")
            print(hero_subtitle.value_of_css_property('line-height'))
            hero_subtitle.screenshot("title.png")
        if hero_subtitle_spaceletter != hero_subtitle.value_of_css_property('letter-spacing'):
            print("Es distinto el letter spacing del title")
            print(hero_subtitle.value_of_css_property('letter-spacing'))
            hero_subtitle.screenshot("title.png")

    def test_tipoLF(self):
        self.driver.implicitly_wait(10)
        leftRight_title = self.driver.find_elements_by_id()
        leftRight_title_fontfamily = "Campaign, sans-serif"
        leftRight_title_fontsize = "35px"
        leftRight_title_lineheight = "40px"
        leftRight_title_spaceletter = "normal"
        if leftRight_title_fontfamily != leftRight_title.value_of_css_property('font-family'):
            print("Son distintos los font family title")
            print(leftRight_title.value_of_css_property('font-family'))
            leftRight_title.screenshot("title.png")
        if leftRight_title_fontsize != leftRight_title.value_of_css_property('font-size'):
            print("Son distintos los font size del title")
            print(leftRight_title.value_of_css_property('font-size'))
            leftRight_title.screenshot("title.png")
        if leftRight_title_lineheight != leftRight_title.value_of_css_property('line-height'):
            print("Son distintos del title")
            print(leftRight_title.value_of_css_property('line-height'))
            leftRight_title.screenshot("title.png")
        if leftRight_title_spaceletter != leftRight_title.value_of_css_property('letter-spacing'):
            print("Es distinto el letter spacing del title")
            print(leftRight_title.value_of_css_property('letter-spacing'))
            leftRight_title.screenshot("title.png")

        leftRight_copy = self.driver.find_elements_by_id()
        leftRight_copy_fontfamily = "Campaign, sans-serif"
        leftRight_copy_fontsize = "35px"
        leftRight_copy_lineheight = "40px"
        leftRight_copy_spaceletter = "normal"
        if leftRight_copy_fontfamily != leftRight_copy.value_of_css_property('font-family'):
            print("Son distintos los font family copy LF")
            print(leftRight_copy.value_of_css_property('font-family'))
            leftRight_copy.screenshot("copyLR.png")
        if leftRight_copy_fontsize != leftRight_copy.value_of_css_property('font-size'):
            print("Son distintos los font size del copy LF")
            print(leftRight_copy.value_of_css_property('font-size'))
            leftRight_copy.screenshot("copyLR.png")
        if leftRight_copy_lineheight != leftRight_copy.value_of_css_property('line-height'):
            print("Son distintos los line height del copy LF")
            print(leftRight_copy.value_of_css_property('line-height'))
            leftRight_copy.screenshot("copyLR.png")
        if leftRight_copy_spaceletter != leftRight_copy.value_of_css_property('letter-spacing'):
            print("Es distinto el letter spacing del copy LF")
            print(leftRight_copy.value_of_css_property('letter-spacing'))
            leftRight_copy.screenshot("copyLF.png")

        images = self.driver.find_elements_by_tag_name('img')
        for img in images:
            dimensions = img.size
            width = dimensions['width']
            height = dimensions['height']
            print('{}x{}'.format(width, height))

    def test_footer(self):
        footer_linktext = self.driver.find_elements_by_id()
        footer_linktext_fontfamily = "Campaign, sans-serif"
        footer_linktext_fontsize = "14px"
        footer_linktext_lineheight = "22px"
        footer_linktext_spaceletter = "normal"
        if footer_linktext_fontfamily != footer_linktext.value_of_css_property('font-family'):
            print("Son distintos los font family linktext footer")
            print(footer_linktext.value_of_css_property('font-family'))
            footer_linktext.screenshot("linktext_footer.png")
        if footer_linktext_fontsize != footer_linktext.value_of_css_property('font-size'):
            print("Son distintos los font size del linktext footer")
            print(footer_linktext.value_of_css_property('font-size'))
            footer_linktext.screenshot("linktext_footer.png")
        if footer_linktext_lineheight != footer_linktext.value_of_css_property('line-height'):
            print("Son distintos los line height del linktext footer")
            print(footer_linktext.value_of_css_property('line-height'))
            footer_linktext.screenshot("linktext_footer.png")
        if footer_linktext_spaceletter != footer_linktext.value_of_css_property('letter-spacing'):
            print("Es distinto el letter spacing del linktext footer")
            print(footer_linktext.value_of_css_property('letter-spacing'))
            footer_linktext.screenshot("linktext_footer.png")

        footer_direcciones = self.driver.find_elements_by_id()
        footer_direcciones_fontfamily = "Campaign, sans-serif"
        footer_direcciones_fontsize = "10px"
        footer_direcciones_lineheight = "11px"
        footer_direcciones_spaceletter = "normal"
        if footer_direcciones_fontfamily != footer_direcciones.value_of_css_property('font-family'):
            print("Son distintos los font family footer direcciones")
            print(footer_direcciones.value_of_css_property('font-family'))
            footer_direcciones.screenshot("footer_direcciones.png")
        if footer_direcciones_fontsize != footer_direcciones.value_of_css_property('font-size'):
            print("Son distintos los font size del footer_direcciones")
            print(footer_direcciones.value_of_css_property('font-size'))
            footer_direcciones.screenshot("footer direcciones.png")
        if footer_direcciones_lineheight != footer_direcciones.value_of_css_property('line-height'):
            print("Son distintos los line height del footer_direcciones")
            print(footer_direcciones.value_of_css_property('line-height'))
            footer_direcciones.screenshot("footer_direcciones.png")
        if footer_direcciones_spaceletter != footer_direcciones.value_of_css_property('letter-spacing'):
            print("Es distinto el letter spacing del footer direcciones")
            print(footer_direcciones.value_of_css_property('letter-spacing'))
            footer_direcciones.screenshot("footer_direcciones.png")

        footer_copyright = self.driver.find_elements_by_id()
        footer_copyright_fontfamily = "Campaign, sans-serif"
        footer_copyright_fontsize = "10px"
        footer_copyright_lineheight = "11px"
        footer_copyright_spaceletter = "normal"
        if footer_copyright_fontfamily != footer_copyright.value_of_css_property('font-family'):
            print("Son distintos los font family copyright footer")
            print(footer_copyright.value_of_css_property('font-family'))
            footer_copyright.screenshot("copyright_footer.png")
        if footer_copyright_fontsize != footer_copyright.value_of_css_property('font-size'):
            print("Son distintos los font size del copyright footer")
            print(footer_copyright.value_of_css_property('font-size'))
            footer_copyright.screenshot("copyright_footer.png")
        if footer_copyright_lineheight != footer_copyright.value_of_css_property('line-height'):
            print("Son distintos los line height del copyright footer")
            print(footer_copyright.value_of_css_property('line-height'))
            footer_copyright.screenshot("copyright_footer.png")
        if footer_copyright_spaceletter != footer_copyright.value_of_css_property('letter-spacing'):
            print("Es distinto el letter spacing del copyright footer")
            print(footer_copyright.value_of_css_property('letter-spacing'))
            footer_copyright.screenshot("copyright_footer.png")