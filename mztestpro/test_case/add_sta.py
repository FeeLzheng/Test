import unittest, random ,sys
from time import sleep

from selenium.webdriver import ActionChains

sys.path.append('C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\')
sys.path.append("./page_obj")
sys.path.append("./models")
sys.path.append("./mztestpro")
from page_obj import base
from page_obj.addPage import add
from page_obj.addPage import edit
from page_obj.loginPage import login
from models import myunit,function,DB

class addTest(myunit.MyTest):
    """注册界面"""





    def test_add1(self):
        """3.1.1 添加员工"""
        DB.delete_conn()
        a ="1"
        login(self.driver).login("417155288@qq.com","test1234")
        add(self.driver).add_createEmployee_click()
        add(self.driver).add_employeeName("1zheng_ceshi"+a+"")
        add(self.driver).add_employeeTime_click()
        add(self.driver).add_employeeTime_chose()
        add(self.driver).add_employeeNo("SS001")
        add(self.driver).add_employeePhone("18966783654")
        add(self.driver).add_employeePosition("测试")
        add(self.driver).add_employeeEmail("88818@uni-ubi.com")
        add(self.driver).add_employeeBornTime_click()
        add(self.driver).add_employeeBornTime_chose()
        add(self.driver).add_employeeHome("温州")
        add(self.driver).add_button()
        add(self.driver).add_picture()
        add(self.driver).add_cancel()
        self.assertEqual(add(self.driver).add_createEmployee(),"+添加人员")
        function.insert_img(self.driver,"123.jpg")




    def test_add2(self):
        """3.1.2 添加9个员工"""
        login(self.driver).login("417155288@qq.com","test1234")
        a = 18966793644
        for i in range(9):
            a=a+1
            a=str(a)
            i=str(i)
            add(self.driver).add_createEmployee_click()
            add(self.driver).add_employeeName("1zheng_ceshi1"+i+"")
            add(self.driver).add_employeeTime_click()
            add(self.driver).add_employeeTime_chose()
            add(self.driver).add_employeeNo("SS0011"+i+"")
            add(self.driver).add_employeePhone(a)
            add(self.driver).add_employeePosition("测试")
            add(self.driver).add_employeeEmail("88881"+i+"@uni-ubi.com")
            add(self.driver).add_employeeBornTime_click()
            add(self.driver).add_employeeBornTime_chose()
            add(self.driver).add_employeeHome("温州")
            add(self.driver).add_button()
            add(self.driver).add_picture()
            add(self.driver).add_cancel()
            a=int(a)
            function.insert_img(self.driver, "1234.jpg")

    def test_add3(self):
        """查看员工信息是否和添加时一致"""
        login(self.driver).login("417155288@qq.com", "test1234")
        #edit(self.driver).edit_employee_text("1zheng_ceshi1","2016-10-31","SS001","18966783654","测试","2016-11-02","88818@uni-ubi.com","温州")
        edit(self.driver).edit_employeeButton()
        self.assertEqual(edit(self.driver).edit_employeeName_text(), "1zheng_ceshi1")
        self.assertEqual( "SS001", edit(self.driver).edit_employeeNo_text())
        self.assertEqual( "18966783654", edit(self.driver).edit_employeePhone_text())
        self.assertEqual("测试", edit(self.driver).edit_employeePosition_text())
        self.assertEqual("88818@uni-ubi.com", edit(self.driver).edit_employeeEmail_text())
        self.assertEqual("温州", edit(self.driver).edit_employeeHome_text())
        edit(self.driver).edit_button()


    def test_add4(self):
        """修改员工内容并且检查是否修改成功"""
        login(self.driver).login("417155288@qq.com", "test1234")
        edit(self.driver).edit_employee("1zheng_ceshi12", "SS0012", "18066783654", "测试2", "888182@uni-ubi.com", "温州2")
        sleep(5)
        edit(self.driver).edit_employeeButton()
        self.assertEqual(edit(self.driver).edit_employeeName_text(), "1zheng_ceshi12")
        #self.assertEqual("2016-10-31", edit(self.driver).edit_employeeTime_text())
        self.assertEqual( "SS0012", edit(self.driver).edit_employeeNo_text())
        self.assertEqual( "18066783654", edit(self.driver).edit_employeePhone_text())
        self.assertEqual("测试2", edit(self.driver).edit_employeePosition_text())
        #self.assertEqual("2016-11-02", edit(self.driver).edit_employeeBornTime_text())
        self.assertEqual("888182@uni-ubi.com", edit(self.driver).edit_employeeEmail_text())

        self.assertEqual("温州2", edit(self.driver).edit_employeeHome_text())
        edit(self.driver).edit_button()
        sleep(3)

    def test_add5(self):
        """停用员工"""
        login(self.driver).login("417155288@qq.com", "test1234")
        edit(self.driver).resign_employee()
        edit(self.driver).resgin_employeeButton()
        sleep(3)
        edit(self.driver).edit_employeeButton()
        self.assertNotEqual(edit(self.driver).edit_employeeName_text(), "1zheng_ceshi12")
        edit(self.driver).edit_button()


    def test_add6(self):
        """增加部门,包括平级，上级，下级"""
        login(self.driver).login("417155288@qq.com", "test1234")
        add(self.driver).add_department()
        add(self.driver).add_departmentSibling()
        add(self.driver).edit_department()
        add(self.driver).delete_department()















if __name__=="__main__":
    unittest.main()