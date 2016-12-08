from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\page_obj")
from base import Page
from time import sleep


class login(Page):
    """用户登录界面
    """

    url ="/"

    # Action
    login_username_loc= (By.NAME,"email")
    login_password_loc=(By.ID,"password")
    login_button_loc=(By.LINK_TEXT,"登录")
    login_verify_loc=(By.ID,"captcha")
    welcome_back_loc=(By.XPATH,"//form[@id='login_form']/div")

# 用户名登入
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

# 登入密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

#鼠标点击用户名
    def login_username_click(self):
        self.find_element(*self.login_username_loc).click()

#鼠标点击密码
    def login_password_click(self):
        self.find_element(*self.login_password_loc).click()

#输入验证码
    def login_verify(self):
        self.find_element(*self.login_verify_loc).send_keys("qqqq")


# 点击登入按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

#定义统一登入入口
    def user_login(self,username="222",password="222"):
        """获取用户名密码登入"""
#登入界面的欢迎回来字样
    def welcome_back(self):
        return self.find_element(*self.welcome_back_loc).text

    def login(self,username,password):
       # self.open()
        self.login_username(username)
        self.login_password(password)
        sleep(10)
        #self.login_verify()
        self.login_button()
        sleep(2)

    user_error_hint_loc=(By.XPATH,"/html/body/div[2]/form/div[2]/span")
    password_error_hint_loc = (By.XPATH,"/html/body/div[2]/form/div[3]/span")
    verify_error_hint_loc=(By.XPATH,"/html/body/div[2]/form/div[5]")


#用户错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text
        print(self.find_element(*self.user_error_hint_loc).text)
    def password_error_hint(self):
        return self.find_element(*self.password_error_hint_loc).text
    def verify_error_hint(self):
        return self.find_element(*self.verify_error_hint_loc).text

#登入成功后的标题
    title_logo_loc=(By.XPATH,"/html/body/div[1]/div[1]/div")

    def title_logo(self):
        return self.find_element(*self.title_logo_loc).text
