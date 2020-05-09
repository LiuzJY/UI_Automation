import unittest
import sys
from time import sleep

sys.path.append('./models')
sys.path.append('./page_obj')
from models import function, myunit
from page_obj.remandPage import remand
from page_obj.loginPage import login


class remandTest(myunit.MyTest):
    def user_login_remand(self, username='', password=''):
        login(self.driver).user_login(username, password)
        sleep(2)
        login(self.driver).guide_button()
        sleep(1)

    def test_remand1(self):
        """正确发布"""
        self.user_login_remand(username='ckg', password='1')
        rf = remand(self.driver)
        rf.remand_button()
        rf.remand_aims()
        rf.remand_price()
        rf.remand_deadline()
        rf.remand_type()
        rf.remand_schedule()
        rf.remand_add()
        rf.remand_release()
        rf.remand_confirm()
        rf.remand_pay()
        sleep(3)


if __name__ == '__main__':
    unittest.main()
