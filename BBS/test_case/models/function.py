from selenium import webdriver
import os


def insert_image(driver_img, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('test_case')[0]
    file_path = base + "report/image/" + file_name
    driver_img.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_image(driver, 'baidu.png')
    driver.quit()
