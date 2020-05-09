from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base import Page
from time import sleep


class login(Page):
    url = '/'
    login_username_loc = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[3]/input[1]')
    login_password_loc = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[3]/input[2]')
    login_button_loc = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[5]')
    guide_button_loc = (By.XPATH, '//*[@id="root"]/div/div/div[7]/div[1]/div/div[2]')

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def guide_button(self):
        self.find_element(*self.guide_button_loc).click()

    def user_login(self, username='username', password='11111'):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH, '/html/body/div[2]')
    password_error_hint_loc = (By.XPATH, '/html/body/div[2]')
    user_login_success_loc = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/a')

    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    def password_error_hint(self):
        return self.find_element(*self.password_error_hint_loc).text

    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
