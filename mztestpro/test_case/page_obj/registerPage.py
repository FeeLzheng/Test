from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\page_obj")
from base import Page
from time import sleep
from loginPage import login


class register(Page):
    """注册界面
    """

    url ="/"

    # Action
    register_companyName_loc=(By.ID,"companyName")
    register_loginName_loc= (By.ID,"loginName")
    register_password_loc=(By.ID,"password")
    register_loc=(By.LINK_TEXT,"还没有账号？立即注册")
    register_captcha_loc = (By.ID, "captcha")
    register_button_loc=(By.LINK_TEXT,"确定")




#鼠标点击注册按钮
    def register_click(self):
        self.find_element(*self.register_loc).click()

#输入公司名字
    def register_companyName(self):
        self.find_element(*self.register_companyName_loc)

#输入用户邮箱
    def register_loginName(self,email):
        self.find_element(*self.register_loginName_loc).send_keys(email)
#输入密码
    def register_password(self,password):
        self.find_element(*self.register_password_loc).send_keys(password)
#输入验证码
    def register_captcha(self):
        self.find_element(*self.register_captcha_loc).send_keys("qqqq")
#点击公司名字
    def register_companyName_click(self):
        self.find_element(*self.register_companyName_loc).click()
#点击用户邮箱
    def register_loginName_click(self):
        self.find_element(*self.register_loginName_loc).click()
#点击密码
    def register_password_click(self):
        self.find_element(*self.register_password_loc).click()

 # 点击确认
    def register_button(self):
        self.find_element(*self.register_button_loc).click()

#定义统一注册

    def register_verify(self,companyName,loginName,password):
       # self.open()
        self.register_companyName(companyName)
        self.register_loginName(loginName)
        self.register_password(password)
        self.register_captcha()
        self.register_button()
        sleep(2)

    register_companyName_loc=(By.XPATH,"/html/body/div[2]/form/div[2]/span[2]")
    register_loginName_loc = (By.XPATH,"/html/body/div[2]/form/div[3]/span[2]")
    register_password_loc=(By.XPATH,"/html/body/div[2]/form/div[4]/span[2]")
    register_error_message=(By.XPATH,"/html/body/div[2]/form/div[6]")

#公司名出错
    def register_companyName_error(self):
        return self.find_element(*self.register_companyName_loc).text
#邮箱出错
    def register_loginName_error(self):
        return self.find_element(*self.register_loginName_loc).text
#密码出错
    def register_password_error(self):
        return self.find_element(*self.register_password_loc).text

#注册失败
    def error_message(self):
        self.find_element(*self.register_error_message)


#注册成功后登入
    def register_login(self,username,password):
        login(self.driver).login(username,password)

# 注册界面的标题
    register_title_loc = (By.XPATH, "/html/body/div[2]/form/div[1]")

    def register_tittle(self):
        return self.find_element(*self.register_title_loc).text
#注册成功后点击返回
    return_back_loc=(By.XPATH,"/html/body/div[1]/a/img")

    def return_back_click(self):
        self.find_element(*self.return_back_click).click()


#登入成功后的标题
    title_logo_loc = (By.XPATH, "/html/body/div[1]/div[1]/div")

    def title_logo(self):
        return self.find_element(*self.title_logo_loc).text

#登入界面的欢迎回来字样
    welcome_back_loc = (By.XPATH, "//form[@id='login_form']/div")

    def welcome_back(self):
        return self.find_element(*self.welcome_back_loc).text

#退出登入
    abbreviation_loc =(By.XPATH,"/html/body/div[1]/div[1]/ul")

    exit_loc=(By.XPATH,"/html/body/div[1]/div[1]/ul/li[1]/a")

    def abbreviation(self):
        self.find_element(*self.abbreviation_loc)
    def exit(self):
        self.find_element(*self.exit_loc).click()


