from time import sleep


class Page(object):

    bbs_url = 'http://www.51hangyu.com/chat'

    def __init__(self, selenium_driver, base_url=bbs_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        print(self.base_url)
        sleep(2)
        assert self.on_page(), 'Did not land on %s' % self.base_url

    def find_element(self, *loc):
        return self.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def find_element_css_selector(self, *loc):
        return self.driver.find_element_by_css_selector(*loc)

    def open(self):
        self._open(self.url)
        # self._open()

    def on_page(self):
        return self.driver.current_url == self.base_url + '/'

    def script(self, src):
        return self.driver.execute_script(src)
