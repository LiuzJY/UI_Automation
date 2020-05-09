from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import os
import time


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.exmail.qq.com")
    smtp.login("jy_liu@taimei-air.com", "LiuJY.1994")
    smtp.sendmail("jy_liu@taimei-air.com", "2212627962@qq.com", msg.as_string())
    smtp.quit()
    print("email send success!")


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './BBS/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="自动化测试报告",
                            description='环境：Windows10，浏览器：Chrome')
    discover = unittest.defaultTestLoader.discover('./BBS/test_case', pattern='*sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./BBS/report/')
    send_mail(file_path)
