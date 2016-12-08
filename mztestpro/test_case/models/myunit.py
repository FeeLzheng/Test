from selenium import webdriver
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\driver")
from driver import browser
import unittest
import time

import os

class MyTest(unittest.TestCase):
    def setUp(self):
       # self.driver = browser()
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://192.168.1.29:8888/SmartStage-Web/admin/employee/index")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()