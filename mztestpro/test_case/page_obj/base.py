class Page(object):
    """"页面基础类，用作所有页面的操作"""

    bbs_url= "http://uface.uni-ubi.com/SmartStage-Web/home/"

    def __init__(self,selenium_driver,base_url=bbs_url, parent=None):
        self.base_url=base_url
        self.driver= selenium_driver
        self.timeout=30
        self.parent=parent


    def open(self,url):
        url=self.base_url+url
        self.driver.get(url)
        assert self.on_page(), "Did not land on %s" %url

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url+self.url)

    def script(self,src):
        return self.driver.execute_script(src)