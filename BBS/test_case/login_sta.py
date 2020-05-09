from time import sleep
import unittest
import random
import sys

sys.path.append('./models')
sys.path.append("./page_obj")
from models import function, myunit
from page_obj.loginPage import login


class loginTest(myunit.MyTest):
    def user_login_verify(self, username='', password=''):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        """ 用户名与密码不匹配 """
        character = random.choice('qwertyuiopasdfghjklzxcvbnm')
        username = 'zhangsan' + character
        self.user_login_verify(username=username, password="123456")
        po = login(self.driver)
        self.assertEqual(po.password_error_hint(), "账号或密码错误请重新输入!")
        function.insert_image(self.driver, "user_pawd_err.png")

    def test_login2(self):
        """用户名、密码为空登录"""
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(), "请输入账号!")
        function.insert_image(self.driver, "user_pawd_empty.png")

    def test_login3(self):
        """成功登录"""
        self.user_login_verify(username='tv', password='1')
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), "西藏航空 ")
        function.insert_image(self.driver, "login_fail.png")


if __name__ == "__main__":
    unittest.main()
