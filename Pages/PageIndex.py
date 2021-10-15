
import os
class PageIndex:
    def __init__(self,myDriver):
        self.driver = myDriver

    def inicio_sesion(self):
        self.driver.implicitly_wait(5)
        button_AreyouaDoctor = self.driver.find_element_by_xpath('/html[1]/body[1]/header[1]/div[1]/div[1]/div[3]/a[1]')
        button_AreyouaDoctor.click()
        self.driver.implicitly_wait(5)
        button_LogIn = self.driver.find_element_by_xpath('/html[1]/body[1]/header[1]/div[1]/div[1]/div[2]/a[1]')
        button_LogIn.click()

    def meet_our_doctors(self):
        self.driver.implicitly_wait(5)
        our_doctors_button = self.driver.find_element_by_link_text('Our Doctors')
        our_doctors_button.click()



