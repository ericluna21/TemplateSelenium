import time
import unittest
import HtmlTestRunner
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Pages.PageIndex import *


class Doctor_selenium_desktop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.page_index = PageIndex(self.driver)
        self.driver.get('https://doctorpedia:!dp2021!@staging.doctorpedia.com/')

    def test_upload(self):
        self.page_index.inicio_sesion()
        self.driver.implicitly_wait(5)
        user_box = self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/form[1]/div[1]/input[1]')
        pass_box = self.driver.find_element_by_name('pwd')
        submit_button = self.driver.find_element_by_name('wp-submit')
        user_box.send_keys('-tester--22-@gmail.com')
        pass_box.send_keys('test')
        submit_button.click()
        self.driver.implicitly_wait(10)
        profile_check = EC.presence_of_element_located(
            (By.CSS_SELECTOR, '/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/h1[1]'))
        if profile_check:
            print("Se inicio el perfil correctamente")
        else:
            print("Se fallo al iniciar el perfil.")
        my_videos_button = self.driver.find_element_by_link_text('My Videos')
        my_videos_button.click()
        self.driver.implicitly_wait(5)
        upload_videos_button = self.driver.find_element_by_link_text('Upload a Video')
        upload_videos_button.click()
        self.driver.implicitly_wait(5)
        publish_cta = self.driver.find_element_by_id('js-publish-article')
        self.driver.find_element(By.ID, "featuredImage").send_keys(
            "C:\\Users\\ericl\\OneDrive\\Documentos\\Bandicam\\prueba.mp4.mp4")
        title_name = self.driver.find_element_by_id('title')
        title_name.send_keys('Test')
        transcrip_value = self.driver.find_element_by_css_selector(
            'body.doctor-platform-landing-page:nth-child(2) div.large-dashboard--grey:nth-child(2) '
            'div.article-edit.blogging-video-editor:nth-child(4) div.doctor-dashboard.custom-large-container '
            'div.doctor-dashboard__wrapper div.doctor-dashboard__wrapper__body form.form-editor:nth-child(4) '
            'div.row.form-group.video-edit-mobile.mx-0:nth-child(3) '
            'div.upload-video-transcript-container.col-xs-12.col-md-7.pl-0 div:nth-child(2) '
            'div.editor.ql-container.ql-snow:nth-child(5) > div.ql-editor.ql-blank')
        transcrip_value.send_keys('Test_Test_test')
        time.sleep(10)
        actions = ActionChains(self.driver)
        actions.move_to_element(publish_cta)
        publish_cta1 = self.driver.find_element_by_id('js-publish-article')
        publish_cta1.click()
        public_verification_cta = self.driver.find_element_by_id('js-open-verified')
        public_verification_cta.click()
        self.driver.implicitly_wait(5)
        self.driver.implicitly_wait(10)
        go_to_perfil_cta = self.driver.find_element_by_css_selector(
            'body.doctor-platform-landing-page:nth-child(2) div.large-dashboard--grey:nth-child(2) '
            'div.shadow.doctors-shadow:nth-child(9) '
            'div.doctors-add-review-modal.modal-new_article.d-flex.align-items-center '
            'div.modal-new_article__box.d-flex.flex-column.align-items-center.text-center.position-relative.js'
            '-confirm-modal div.modal-new_article__box-cta-container.d-flex.justify-content-center:nth-child(5) > '
            'a.modal-new_article__box-cta:nth-child(1)')
        if go_to_perfil_cta:
            print("El perfil subio correctamente el video")
        else:
            print("El perfil fallo subiendo el archivo")
        go_to_perfil_cta.click()
        self.driver.implicitly_wait(10)
        if profile_check:
            print("Se volvio al inicio correctamente")
        else:
            print("Fallo al volver al perfil")

    def test_drownSpeciality(self):
        self.page_index.meet_our_doctors()
        self.driver.implicitly_wait(5)
        speciality_dropdown = Select(self.driver.find_element_by_name('searchSpecialty'))
        timeout = 13
        for i in range(20):
            speciality_dropdown.select_by_index(i)
            try:
                CardsPerfiles = EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]"))
                WebDriverWait(self.driver, timeout).until(CardsPerfiles)
                self.assertNotEqual(speciality_dropdown.first_selected_option.text.strip(), 'CONGO')
            except TimeoutException:
                print("Timed out waiting for page to load, speciality", i)
                self.driver.get_screenshot_as_file('screenSpeciality.png')
        pass

    def test_drowAreas(self):
        self.driver.implicitly_wait(5)
        our_doctors_button = self.driver.find_element_by_link_text('Our Doctors')
        our_doctors_button.click()
        self.driver.implicitly_wait(5)
        AreasExpertiseDropdown = Select(self.driver.find_element_by_name('searchExpertise'))
        timeout = 13
        for i in range(20):
            AreasExpertiseDropdown.select_by_index(i)

            try:
                CardsPerfiles = EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]"))
                WebDriverWait(self.driver, timeout).until(CardsPerfiles)

            except TimeoutException:
                print("Timed out waiting for page to load, AreasExpertise", i)
                self.driver.get_screenshot_as_file('screenAreasExpertiseDropdown.png')

    def test_drowName(self):
        self.driver.implicitly_wait(5)
        our_doctors_button = self.driver.find_element_by_link_text('Our Doctors')
        our_doctors_button.click()
        self.driver.implicitly_wait(5)
        Doctorname = Select(self.driver.find_element_by_name('filterByExpert'))
        timeout = 13
        for i in range(20):
            try:
                Doctorname.select_by_index(i)
                CardsPerfiles = EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]"))
                WebDriverWait(self.driver, timeout).until(CardsPerfiles)
            except TimeoutException:
                print("Timed out waiting for page to load, Doctorname", i)
                self.driver.get_screenshot_as_file('screenDoctorname.png')

    def testSearch(self):
        search = self.driver.find_element_by_name('condition')
        search.send_keys('Covid')
        search.send_keys(Keys.ENTER)
        time.sleep(10)
        timeout = 5
        Resultado = EC.presence_of_element_located((By.CSS_SELECTOR, "#js-search-condition"))
        WebDriverWait(self.driver, timeout).until(Resultado)
        self.driver.get_screenshot_as_file('Search.png')

    def test_filtrosperfiles(self):
        self.page_index.meet_our_doctors()
        self.driver.implicitly_wait(5)
        link_doctor = self.driver.find_element_by_class_name('click-avatar')
        link_doctor.click()
        self.driver.implicitly_wait(6)
        filtro_videos = self.driver.find_element_by_xpath('//li[contains(text(),"VIDEOS")]')
        filtro_videos.click()
        time.sleep(5)
        tag_videos = self.driver.find_element_by_class_name('video-profile__body')
        self.driver.get_screenshot_as_file('Tag.png')
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
