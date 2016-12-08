from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\page_obj")
from base import Page
from time import sleep
from loginPage import login


class forget(Page):
    """忘记密码界面
    """

    url ="/"

    # Action

    forget_username_loc= (By.NAME,"email")
    forget_password_loc=(By.ID,"password")
    forget_button_loc=(By.CLASS_NAME,"reset")
    forget_captcha_loc = (By.ID, "captcha")
    forget_button_loc=(By.LINK_TEXT,"确定")




#鼠标点击忘记密码按钮
    def forget_click(self):
        self.find_element(*self.forget_button_loc).click()

#输入用户邮箱
    def forget_username(self,username):
        self.find_element(*self.forget_username_loc).send_keys(username)
#输入新密码
    def forget_password(self,password):
        self.find_element(*self.forget_password_loc).send_keys(password)
#输入验证码
    def forget_captcha(self):
        self.find_element(*self.forget_captcha_loc).send_keys("qqqq")

#点击用户邮箱
    def forget_username_click(self):
        self.find_element(*self.forget_username_loc).click()
#点击新密码
    def forget_password_click(self):
        self.find_element(*self.forget_password_loc).click()
#点击确认
    def forget_button(self):
        self.find_element(*self.forget_button_loc).click()

#定义统一修改

    def user_forget(self,username,password):
       # self.open()
        self.forget_username(username)
        self.forget_password(password)
        self.forget_captcha()
        self.forget_button()
        sleep(2)

    forget_username_error_loc=(By.XPATH,"/html/body/div[2]/form/div[2]/span[2]")
    forget_password_error_loc = (By.XPATH,"/html/body/div[2]/form/div[4]/span[2]")
    forget_captcha_error_loc=(By.XPATH,"/html/body/div[2]/form/div[5]")

#用户错误提示
    def forget_username_error(self):
        return self.find_element(*self.forget.username_error_loc).text
    def forget_password_error(self):
        return self.find_element(*self.forget_password_error_loc).text
    def forget_error(self):
        return self.find_element(*self.forget_captcha_error_loc).text

#修改成功后重新登入
    def second_login(self,username,password):
        login(self.driver).login(username,password)

# 忘记密码界面的标题
    forget_title_loc = (By.XPATH, "/html/body/div[2]/form/div[1]")

    def forget_title(self):
        return self.find_element(*self.forget_title_loc).text

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


#忘记密码界面的忘记密码字样
    forget_text_loc = (By.XPATH, "/html/body/div[2]/form/div[1]")

    def forget_text(self):
        return self.find_element(*self.forget_text_loc).text