import unittest, random ,sys
sys.path.append('C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\')
sys.path.append("./page_obj")
sys.path.append("./models")
sys.path.append("./mztestpro")
from page_obj import base
from page_obj.loginPage import login
from models import myunit,function

class loginTest(myunit.MyTest):
    """登录界面"""
    # 测试用户登入
    def user_login_verify(self,username,password):
        login(self.driver).user_login(username,password)


    # 用户邮箱
    def user_login_verify_username(self,username):
        login(self.driver).login_username(username)

    # 点击用户邮箱
    def user_login_click_username(self):
        login(self.driver).login_username_click()

        # 点击用户密码

    def user_login_click_password(self):
        login(self.driver).login_password_click()

    # 用户密码
    def user_login_verify_password(self, password):
            login(self.driver).login_password(password)

    def test_login1(self):
        """1.1.1 用户名和密码为空"""
        login(self.driver).login_verify()
        login(self.driver).login_button()
        self.assertEqual(login(self.driver).welcome_back(), "欢迎回来")
        self.assertNotEqual(login(self.driver).title_logo(),"Uface智能前台管理系统")
        function.insert_img(self.driver,"1.1.1_email_password_empty.jpg")

    def test_login2(self):
        """1.1.2 邮箱格式错误01：741562314@qq.com2"""
        self.user_login_verify_username("741562314@qq.com2")
        self.user_login_click_password()
        self.assertEqual(login(self.driver).user_error_hint(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"1.1.2_email_error01.jpg")

    def test_login3(self):
        """1.1.3 邮箱格式错误02：741562314qq.com"""
        self.user_login_verify_username("741562314@qq.com2")
        self.user_login_click_password()
        self.assertEqual(login(self.driver).user_error_hint(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"1.1.3_email_error02.jpg")

    def test_login4(self):
        """1.1.4 邮箱格式大写：741562314@QQ.COM"""
        self.user_login_verify_username("741562314@QQ.COM")
        self.user_login_click_password()
        self.assertNotEqual(login(self.driver).user_error_hint(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"1.1.4_email_capital.jpg")

    def test_login5(self):
        """1.1.5 邮箱格式大小写并存：741562314@Qq.CoM"""
        self.user_login_verify_username("741562314@Qq.CoM")
        self.user_login_click_password()
        self.assertNotEqual(login(self.driver).user_error_hint(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"1.1.5_email_capital_lower.jpg")

    def test_login6(self):
        """1.1.6 改正错误格式邮箱错误提示消失：741562314@qq.com2->741562314@qqq.com"""
        self.user_login_verify_username("741562314@qq.com2")
        self.user_login_click_password()
        self.assertEqual(login(self.driver).user_error_hint(),"* 邮箱地址格式错误")
        function.insert_img(self.driver, "1.1.6_email_incorrect.jpg")
        self.user_login_verify_username("741562314@qq.com")
        self.user_login_click_password()
        self.assertNotEqual(login(self.driver).user_error_hint(), "* 邮箱地址格式错误")
        function.insert_img(self.driver,"1.1.6_email_correct.jpg")

    def test_login7(self):
        """1.2.1 密码格式错误01:无字母下划线和数字"""
        self.user_login_verify_password("@@@@@@@@")
        self.user_login_click_username()
        self.assertEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.1 password_error01.jpg")

    def test_login8(self):
        """1.2.2 密码格式错误02:密码大于16位"""
        self.user_login_verify_password("12345678901234567")
        self.user_login_click_username()
        self.assertEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.2 password_error02.jpg")

    def test_login9(self):
        """1.2.3 密码格式错误03:密码小于8位"""
        self.user_login_verify_password("1234567")
        self.user_login_click_username()
        self.assertEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.3 password_error03.jpg")

    def test_login10(self):
        """1.2.4 密码格式正确01:只有下划线"""
        self.user_login_verify_password("________")
        self.user_login_click_username()
        self.assertNotEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.4 password_correct01.jpg")

    def test_login11(self):
        """1.2.5 密码格式正确02:只有数字"""
        self.user_login_verify_password("________")
        self.user_login_click_username()
        self.assertNotEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.5 password_correct02.jpg")

    def test_login12(self):
        """1.2.6 密码格式正确03:只有字母"""
        self.user_login_verify_password("aaaaAAAA")
        self.user_login_click_username()
        self.assertNotEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.6 password_correct03.jpg")

    def test_login13(self):
        """1.2.7 密码格式正确04:只有大小写字母和数字"""
        self.user_login_verify_password("aaaaAA11")
        self.user_login_click_username()
        self.assertNotEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.7 password_correct04.jpg")

    def test_login14(self):
        """1.2.8 密码格式正确05:只有大小写字母和数字"""
        self.user_login_verify_password("AAAAA1111")
        self.user_login_click_username()
        self.assertNotEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.8 password_correct05.jpg")

    def test_login15(self):
        """1.2.9 密码格式正确06:数字字母下划线都存在"""
        self.user_login_verify_password("AAAA__111")
        self.user_login_click_username()
        self.assertNotEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.9 password_correct06.jpg")

    def test_login16(self):
        """1.2.10 修改错误格式密码后错误提示消失"""
        self.user_login_verify_password("AAAA")
        self.user_login_click_username()
        self.assertEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver, "1.2.10 password_incorrect07.jpg")
        self.user_login_verify_password("test1234")
        self.user_login_click_username()
        self.assertNotEqual(login(self.driver).password_error_hint(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"1.2.10 password_correct07.jpg")

    def test_login17(self):
        """1.3.1 邮箱正确，密码不正确01:原密码为小写字母，输入密码为大写"""
        self.user_login_verify("74156234@qq.com","TEST1234")
        self.assertEqual(login(self.driver).welcome_back(),"欢迎回来")
        self.assertEqual(login(self.driver).verify_error_hint(), "用户名或密码错误")
        function.insert_img(self.driver,"1.3.1_login_fail01.jpg")

    def test_login18(self):
        """1.3.2 邮箱正确，密码不正确02:与原密码不匹配的密码"""
        self.user_login_verify("74156234@qq.com","test12345")
        self.assertEqual(login(self.driver).welcome_back(), "欢迎回来")
        self.assertEqual(login(self.driver).verify_error_hint(), "用户名或密码错误")
        function.insert_img(self.driver,"1.3.2_login_fail02.jpg")

    def test_login19(self):
        """1.3.3 邮箱和密码都不正确"""
        self.user_login_verify("741562345@qq.com","test12345")
        self.assertEqual(login(self.driver).welcome_back(), "欢迎回来")
        self.assertEqual(login(self.driver).verify_error_hint(), "用户名或密码错误")
        function.insert_img(self.driver,"1.3.3_login_fail03.jpg")

    def test_login20(self):
        """1.3.4 密码格式正确："""
        self.user_login_verify("741562314@qq.com","test1234")
        self.assertNotEqual(login(self.driver).welcome_back(), "欢迎回来")
        self.assertEqual(login(self.driver).title_logo(),"Uface智能前台管理系统")
        function.insert_img(self.driver,"1.3.4_login_success.jpg")



if __name__=="__main__":
    unittest.main()