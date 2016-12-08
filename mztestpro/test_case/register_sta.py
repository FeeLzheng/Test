import unittest, random ,sys

from selenium.webdriver import ActionChains

sys.path.append('C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\')
sys.path.append("./page_obj")
sys.path.append("./models")
sys.path.append("./mztestpro")
from page_obj import base
from page_obj.registerPage import register
from page_obj.loginPage import login
from models import myunit,function

class registerTest(myunit.MyTest):
    """注册界面"""

    #点击注册账号

    def register_click(self):
        register(self.driver).register_click()

    # 测试用户修改密码

    def register(self,companyName,loginName,passowrd):
        register(self.driver).register_verify(companyName,loginName,passowrd)

    #输入公司名字

    def register_verify_companyName(self,company):
        register(self.driver).register_companyName(company)

    #点击公司名字

    def register_companyName_click(self):
        register(self.driver).register_companyName_click()

    # 输入用户邮箱
    def register_verify_loginName(self,loginName):
        register(self.driver).register_loginName(loginName)

    # 点击用户邮箱
    def register_loginName_click(self):
        register(self.driver).register_loginName_click()

     #点击用户密码

    def register_password_click(self):
        register(self.driver).register_password_click()

    # 输入用户密码
    def register_verify_password(self, password):
        register(self.driver).register_password(password)

    # 悬浮操作

    def abbreviation(self):
        above=register(self.driver).abbreviation()
        ActionChains(self.driver).move_to_element(above).perform()

    def test_register1(self):
        """3.1.1 英文公司名:StateStreet"""
        self.register_click()
        self.register_verify_companyName("StateStreet")
        self.register_loginName_click()
        self.assertNotEqual(register(self.driver).register_companyName_error(),"* 公司名称字数不能超过30个")
        function.insert_img(self.driver,"3.1.1_companyName_English.jpg")

    def test_register2(self):
        """3.1.2 英文公司名：杭州宇泛智能科技有限公司"""
        self.register_click()
        self.register_verify_companyName("杭州宇泛智能科技有限公司")
        self.register_loginName_click()
        self.assertNotEqual(register(self.driver).register_companyName_error(),"* 公司名称字数不能超过30个")
        function.insert_img(self.driver,"3.1.2_company_Chinese.jpg")

    def test_register3(self):
        """3.1.3 英文公司名个数大于30个：741562314qq.com"""
        self.register_click()
        self.register_verify_companyName("abcdefghijklmnopqistuvwsyzaaaaaaaaaaaa")
        self.register_loginName_click()
        self.assertEqual(register(self.driver).register_companyName_error(),"* 公司名称字数不能超过30个")
        function.insert_img(self.driver,"3.1.3_companyName_EnglishMore.jpg")

    def test_register4(self):
        """3.1.4 中文公司名个数大于30个：字数大于30个字大于30个字大于30个字大于30个字大于30个字大于30个字大于30个字大于30个字"""
        self.register_click()
        self.register_verify_companyName("字数大于30个字大于30个字大于30个字大于30个字大于30个字大于30个字大于30个字大于30个字")
        self.register_loginName_click()
        self.assertEqual(register(self.driver).register_companyName_error(), "* 公司名称字数不能超过30个")
        function.insert_img(self.driver, "3.1.4_companyName_ChineseMore.jpg")


    def test_register5(self):
        """3.2.1 邮箱格式错误01:后缀问题如741562314@qq.com2"""
        self.register_click()
        self.register_verify_loginName("741562314@qq.com2")
        self.register_companyName_click()
        self.assertEqual(register(self.driver).register_loginName_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"3.2.1_email_error01.jpg")

    def test_register6(self):
        """3.2.2 邮箱格式错误02：无@字符 如741562314qq.com"""
        self.register_click()
        self.register_verify_loginName("741562314qq.com")
        self.register_companyName_click()
        self.assertEqual(register(self.driver).register_loginName_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"3.2.2_email_error02.jpg")

    def test_register7(self):
        """3.2.3 邮箱格式大写：741562314@QQ.com"""
        self.register_click()
        self.register_verify_loginName("741562314@QQ.COM")
        self.register_companyName_click()
        self.assertNotEqual(register(self.driver).register_loginName_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"3.2.3_email_capital.jpg")

    def test_register8(self):
        """3.2.4 邮箱格式大小写并存：741562314@Qq.CoM"""
        self.register_click()
        self.register_verify_loginName("741562314@Qq.CoM")
        self.register_companyName_click()
        self.assertNotEqual(register(self.driver).register_loginName_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver,"3.2.4_email_capital_lower.jpg")

    def test_register9(self):
        """3.2.5 改正错误格式邮箱错误提示消失：741562314@qq.com2->741562314@qqq.com"""
        self.register_click()
        self.register_verify_loginName("741562314@qq.com2")
        self.register_companyName_click()
        self.assertEqual(register(self.driver).register_loginName_error(),"* 邮箱地址格式错误")
        function.insert_img(self.driver, "3.2.5_email_incorrect.jpg")
        self.register_verify_loginName("741562314@qq.com")
        self.register_companyName_click()
        self.assertNotEqual(register(self.driver).register_loginName_error(), "* 邮箱地址格式错误")
        function.insert_img(self.driver,"3.2.5_email_correct.jpg")

    def test_register10(self):
        """3.2.6 公司名，邮箱和密码为空"""
        self.register_click()
        register(self.driver).forget_captcha()
        register(self.driver).forget_button()
        self.assertEqual(register(self.driver).register_title(), "创建账号")
        self.assertNotEqual(register(self.driver).welcome_back(),"欢迎回来")
        function.insert_img(self.driver,"3.2.6_email_password_empty.jpg")

    def test_register11(self):
        """3.3.1 密码格式错误01:无字母下划线和数字"""
        self.register_click()
        self.register_verify_password("@@@@@@@@")
        self.register_companyName_click()
        self.assertEqual(register(self.driver).register_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"3.3.1 password_error01.jpg")

    def test_register12(self):
        """3.3.2 密码格式错误02:密码大于16位"""
        self.register_click()
        self.register_verify_password("12345678901234567")
        self.register_companyName_click()
        self.assertEqual(register(self.driver).register_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"3.3.2 password_error02.jpg")

    def test_register13(self):
        """3.3.3 密码格式错误03:密码小于8位"""
        self.register_click()
        self.register_verify_password("1234567")
        self.register_companyName_click()
        self.assertEqual(register(self.driver).register_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"3.3.3 password_error03.jpg")

    def test_register14(self):
        """3.3.4 密码格式正确01:只有下划线"""
        self.register_click()
        self.register_verify_password("________")
        self.register_companyName_click()
        self.assertNotEqual(register(self.driver).register_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"3.3.4 password_correct01.jpg")

    def test_register15(self):
        """3.3.5 密码格式正确02:只有数字"""
        self.register_click()
        self.register_verify_password("1234567890")
        self.register_companyName_click()
        self.assertNotEqual(register(self.driver).register_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"3.3.5 password_correct02.jpg")

    def test_register16(self):
        """3.3.6 密码格式正确03:只有字母"""
        self.register_click()
        self.register_verify_password("aaaaAAAA")
        self.register_companyName_click()
        self.assertNotEqual(register(self.driver).register_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"3.3.6 password_correct03.jpg")

    def test_register17(self):
        """3.3.7 密码格式正确04:只有大小写字母和数字"""
        self.register_click()
        self.register_verify_password("aaaaAA11")
        self.register_companyName_click()
        self.assertNotEqual(register(self.driver).register_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"3.3.7 password_correct04.jpg")

    def test_register18(self):
        """3.3.8 密码格式正确05:只有大小写字母和数字"""
        self.register_click()
        self.register_verify_password("AAAAA1111")
        self.register_companyName_click()
        self.assertNotEqual(register(self.driver).register_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"3.3.8 password_correct05.jpg")

    def test_register19(self):
        """3.3.9 密码格式正确06:数字字母下划线都存在"""
        self.register_click()
        self.register_verify_password("AAAA__111")
        self.register_companyName_click()
        self.assertNotEqual(register(self.driver).register_password_error(),"* 密码格式提示：大、小写字母／数字／下划线，8-16位")
        function.insert_img(self.driver,"3.3.9 password_correct06.jpg")



if __name__=="__main__":
    unittest.main()