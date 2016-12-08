import os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
import unittest
import sys
sys.path.append("D:\\appium\\DK\android-sdk_r23.0.2-windows\android-sdk-windows\platform-tools")

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.5.1'
        desired_caps['deviceName'] = 'vivi-vivo_x7-a635f4b6'
        desired_caps['appPackage'] = 'com.uniubi.attendance'
        desired_caps['appActivity'] = 'com.uniubi.attendance.Activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):

        self.driver.quit()

    def test_add_contacts(self):
        sleep(5)
        Email=self.driver.find_element_by_id("com.uniubi.attendance:id/et_login_username")
        Email.click()
        Email.clear()
        Email.send_keys("18768172337")
        password=self.driver.find_element_by_id("com.uniubi.attendance:id/et_login_passward")
        password.click()
        password.clear()
        password.send_keys("123456")
        self.driver.keyevent(66)
        self.driver.find_element_by_id("com.uniubi.attendance:id/bt_login_enter").click()
        sleep(5)



if __name__ == '__main__':
    testsuite=unittest.TestSuite()
    testsuite.addTest(SimpleAndroidTests("calculator"))
    file_name="./result.html"
    fp= open(file_name,"wb")
    runner =HTMLTestRunner(stream=fp,title="UniUbi登入测试报告",description="环境：W8，浏览器：firefox")
    runner.run(testsuite)

