import unittest, random ,sys

from selenium.webdriver import ActionChains

sys.path.append('C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\')
sys.path.append("./page_obj")
sys.path.append("./models")
sys.path.append("./mztestpro")
from page_obj import base
from page_obj.forgetPage import forget
from models import myunit,function

class forgetTest(myunit.MyTest):
    """ 忘记密码界面"""
    #点击忘记密码

    def forget_click(self):
        forget(self.driver).forget_click()

    # 测试用户修改密码

    def forget_verify(self,username,password):
        forget(self.driver).user_forget(username,password)


    # 输入用户邮箱
    def forget_verify_username(self,username):
        forget(self.driver).forget_username(username)

    # 点击用户邮箱
    def forget_username_click(self):
        forget(self.driver).forget__username_click()

     #点击用户密码

    def forget_password_click(self):
        forget(self.driver).forget_password_click()

    # 用户密码
    def forget_password(self, password):
        forget(self.driver).forget_password(password)

    # 悬浮操作

    def abbreviation(self):
        above=forget(self.driver).abbreviation()
        ActionChains(self.driver).move_to_element(above).perform()

    def test_forget1(self):
        """2.1.1 邮箱格式错误01:后缀问题如741562314@qq.com2"""
        self.forget_click()
        self.forget_verify_username("741562314@qq.com2")
        self.forget_password_click()
        self.assertEqual(forget(self.driver).forget_username_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"2.1.1_email_error01.jpg")

    def test_forget2(self):
        """2.1.2 邮箱格式错误02：无@字符 如741562314qq.com"""
        self.forget_click()
        self.forget_verify_username("741562314qq.com")
        self.forget_password_click()
        self.assertEqual(forget(self.driver).forget_username_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"2.1.2_email_error02.jpg")

    def test_forget3(self):
        """2.1.3 邮箱格式大写：741562314@QQ.com"""
        self.forget_click()
        self.forget_verify_username("741562314@QQ.COM")
        self.forget_password_click()
        self.assertNotEqual(forget(self.driver).forget_username_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"2.1.3_email_capital.jpg")

    def test_forget4(self):
        """2.1.4 邮箱格式大小写并存：741562314@Qq.CoM"""
        self.forget_click()
        self.forget_verify_username("741562314@Qq.CoM")
        self.forget_password_click()
        self.assertNotEqual(forget(self.driver).forget_username_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"2.1.4_email_capital_lower.jpg")


    def test_forget5(self):
        """2.1.5 改正错误格式邮箱错误提示消失：741562314@qq.com2->741562314@qqq.com"""
        self.forget_click()
        self.forget_verify_username("741562314@qq.com2")
        self.forget_password_click()
        self.assertEqual(forget(self.driver).forget_username_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver, "2.1.5_email_incorrect.jpg")
        self.forget_verify_username("741562314@qq.com")
        self.user_login_click_password()
        self.assertNotEqual(forget(self.driver).forget_username_error(), "* 邮箱地址格式错误")
        function.insert_img(self.driver,"2.1.5_email_correct.jpg")

    def test_forget6(self):
        """2.1.6 用户名和密码为空"""
        self.forget_click()
        forget(self.driver).forget_captcha()
        forget(self.driver).forget_button()
        self.assertEqual(forget(self.driver).forget_title(), "忘记密码")
        self.assertNotEqual(forget(self.driver).welcome_back(),"欢迎回来")
        function.insert_img(self.driver,"2.1.6_email_password_empty.jpg")

    def test_forget7(self):
        """2.2.1 密码格式错误01:无字母下划线和数字"""
        self.forget_click()
        self.forget_verify_password("@@@@@@@@")
        self.forget_username_click()
        self.assertEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.1 password_error01.jpg")

    def test_forget8(self):
        """2.2.2 密码格式错误02:密码大于16位"""
        self.forget_click()
        self.forget_verify_password("12345678901234567")
        self.forget_username_click()
        self.assertEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.2 password_error02.jpg")

    def test_forget9(self):
        """2.2.3 密码格式错误03:密码小于8位"""
        self.forget_click()
        self.forget_verify_password("1234567")
        self.forget_username_click()
        self.assertEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.3 password_error03.jpg")

    def test_forget10(self):
        """2.2.4 密码格式正确01:只有下划线"""
        self.forget_click()
        self.forget_verify_password("________")
        self.forget_username_click()
        self.assertNotEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.4 password_correct01.jpg")

    def test_forget11(self):
        """2.2.5 密码格式正确02:只有数字"""
        self.forget_click()
        self.forget_verify_password("1234567890")
        self.forget_username_click()
        self.assertNotEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.5 password_correct02.jpg")

    def test_forget12(self):
        """2.2.6 密码格式正确03:只有字母"""
        self.forget_click()
        self.forget_verify_password("aaaaAAAA")
        self.forget_username_click()
        self.assertNotEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.6 password_correct03.jpg")

    def test_forget13(self):
        """2.2.7 密码格式正确04:只有大小写字母和数字"""
        self.forget_click()
        self.forget_verify_password("aaaaAA11")
        self.forget_username_click()
        self.assertNotEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.7 password_correct04.jpg")

    def test_forget14(self):
        """2.2.8 密码格式正确05:只有大小写字母和数字"""
        self.forget_click()
        self.forget_verify_password("AAAAA1111")
        self.forget_username_click()
        self.assertNotEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.8 password_correct05.jpg")

    def test_forget15(self):
        """2.2.9 密码格式正确06:数字字母下划线都存在"""
        self.forget_click()
        self.forget_verify_password("AAAA__111")
        self.forget_username_click()
        self.assertNotEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.9 password_correct06.jpg")

    def test_forget16(self):
        """2.2.10 修改错误格式密码后错误提示消失"""
        self.forget_click()
        self.forget_verify_password("AAAA")
        self.forget_username_click()
        self.assertEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver, "2.2.10 password_incorrect07.jpg")
        self.forget_verify_password("test1234")
        self.forget_username_click()
        self.assertNotEqual(forget(self.driver).forget_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.2.10 password_correct07.jpg")

    def test_forget17(self):
        """2.3.1 密码与原密码一致:密码与原密码一致"""
        self.forget_click()
        self.user_forget("741562314@qq.com","test1234")
        self.assertNotEqual(forget(self.driver).forget_text(),"忘记密码")
        forget(self.driver).second_login("741562314@qq.com","test1234")
        self.assertEqual(forget(self.driver).title_logo(), "Uface智能前台管理系统")
        function.insert_img(self.driver,"3.3.1_login_success01.jpg")

    def test_forget18(self):
        """2.3.2 账号格式错误，密码正确:74156234@qq2.com","test12345"""
        self.forget_click()
        self.user_forget("74156234@qq2.com","test12345")
        self.assertEqual(forget(self.driver).forget_text(), "欢迎回来")
        self.assertEqual(forget(self.driver).forget_username_error(), "邮箱地址格式错误")
        function.insert_img(self.driver,"2.3.2_forget_fail01.jpg")

    def test_forget19(self):
        """2.3.3 账号格式正确，密码格式不正确:741562345qq.com","test12"""
        self.forget_click()
        self.user_forget("741562345@qq.com","test12")
        self.assertEqual(forget(self.driver).forget_text(), "欢迎回来")
        self.assertNotEqual(forget(self.driver).forget_username_error(), "邮箱地址格式错误")
        self.assertEqual(forget(self.driver).forget_password_error(), "* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.3.3_forget_fail02.jpg")

    def test_forget20(self):
        """2.3.4 账号密码格式都不正确：741562314@qqcom","test12"""
        self.forget_click()
        self.user_login_verify("741562314@qqcom","test12")
        self.assertEqual(forget(self.driver).forget_text(), "欢迎回来")
        self.assertEqual(forget(self.driver).forget_username_error(), "邮箱地址格式错误")
        self.assertEqual(forget(self.driver).forget_password_error(), "* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"2.3.4_forget_fail03.jpg")

    def test_forget17(self):

        """2.3.5 密码与原密码一致:741562314@qq.com", "testaaaa"""
        self.forget_click()
        self.user_forget("741562314@qq.com", "testaaaa")
        self.assertNotEqual(forget(self.driver).forget_text(), "忘记密码")
        forget(self.driver).second_login("741562314@qq.com", "testaaaa")
        self.assertEqual(forget(self.driver).title_logo(), "Uface智能前台管理系统")
        function.insert_img(self.driver, "3.3.5_forget_success01.jpg")
        self.abbreviation()#悬浮
        forget(self.driver).exit()
        self.forget_click()
        self.user_forget("741562314@qq.com", "test1234")
        self.assertEqual(forget(self.driver).welcome_back(), "欢迎回来")
        function.insert_img(self.driver, "3.3.5_forget_success02.jpg")


if __name__=="__main__":
    unittest.main()