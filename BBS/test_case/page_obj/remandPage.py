from .base import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class remand(Page):
    remand_button_loc = (By.XPATH, '//*[@id="nav-box"]/div[2]/div[2]/div[4]/div')

    remand_aims_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div/div[2]/div[2]/input')
    remand_aims_item_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div/div[2]/div[2]/div/div')

    remand_price_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div[1]/div[2]/div[4]/div[2]')
    remand_price_item_loc = (By.XPATH, '/html/body/div[2]/div/div/ul/li[3]')

    plan_add_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div[1]/div[2]/div[5]/div')

    schedule_choose_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div[3]/div[2]/div/input[2]')

    remand_date_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div[4]/div[2]/div[2]/span/div/input')

    remand_type_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div[4]/div[1]/div[2]/input')
    type_item_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div[4]/div[1]/div[2]/div/div[4]')

    remand_release_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div[10]/div[2]/button')

    remand_draft_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div[10]/div[1]/button')

    remand_confirm_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[1]/div/div[3]/div[1]/button')

    remand_pay_password_loc = \
        (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[1]/div/div/div[2]/div[1]/ul/li[1]')
    remand_pay_loc = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/button')

    def remand_button(self):
        self.find_element(*self.remand_button_loc).click()

    # 目标航点
    def remand_aims(self):
        self.find_element(*self.remand_aims_loc).send_keys('通辽机场')
        sleep(1)
        self.find_element(*self.remand_aims_item_loc).click()

    # 需求有效期
    def remand_deadline(self):
        self.find_element(*self.remand_date_loc).click()

    # 机型
    def remand_type(self):
        self.find_element(*self.remand_type_loc).click()
        self.find_element(*self.type_item_loc).click()

    # 班期
    def remand_schedule(self):
        self.find_element(*self.schedule_choose_loc).click()

    # 报价
    def remand_price(self):
        self.find_element(*self.remand_price_loc).click()
        self.find_element(*self.remand_price_item_loc).click()

    # 新增方案
    def remand_add(self):
        self.find_element(*self.plan_add_loc).click()

    # 确认发布
    def remand_release(self):
        self.find_element(*self.remand_release_loc).click()

    # 保存草稿
    def remand_draft(self):
        self.find_element(*self.remand_draft_loc).click()

    # 确认意向金
    def remand_confirm(self):
        self.find_element(*self.remand_confirm_loc).click()

    # 支付密码
    def remand_pay(self):
        # self.find_element(*self.remand_pay_password_loc).click()
        self.find_element(*self.remand_pay_password_loc)
        sleep(1)
        # self.find_element(*self.remand_pay_loc).click()
