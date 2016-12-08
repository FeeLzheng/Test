from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\page_obj")
from base import Page
from time import sleep
from loginPage import login


class add(Page):
    """注册界面
    """

    url ="/"

    # Action
    add_employee_loc=(By.LINK_TEXT,"人事管理")
    add_createEmployee_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/a")
    add_employeeName_loc=(By.ID,"name2")
    add_employeeTime_loc=(By.XPATH,"/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[1]/td[4]/span")
    add_employeeTime_loc1 = (By.ID,"joinDate2")
    time_loc=(By.XPATH,"/html/body/div[4]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/span")
    add_employeeNo_loc=(By.ID,"employeeNo2")
    add_employeePhone_loc = (By.ID, "phone2")
    add_employeeDepartment_loc=(By.XPATH,"/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/ul/input")
    add_employeeSex_loc=(By.XPATH,"/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[3]/td[4]/ul/span")
    add_employeePosition_loc=(By.ID,"position2")
    add_employeeBornTime_loc = (By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[4]/td[4]/span")
    bornTime_loc=(By.XPATH,"/html/body/div[5]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[3]/span")
    add_employeeEmail_loc=(By.ID,"email2")
    add_employeeMarriage_loc=(By.XPATH,"/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[5]/td[4]/ul/span")
    add_employeeEducation_loc=(By.XPATH,"/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[6]/td[2]/ul/span")
    add_employeeHome_loc=(By.ID,"home2")

    add_employeeButton=(By.XPATH,"/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[3]/input[1]")
    add_pictureButton=(By.XPATH,"/html/body/div[1]/div[6]/div[2]/div[2]/div[2]/div[3]")
    add_cancelButton=(By.XPATH,"/html/body/div[1]/div[6]/div[2]/div[2]/div[3]/div[6]/input[2]")
    add_closeButton=(By.CLASS_NAME,"close")



#点击人事模块
    def add_employee_click(self):
        self.find_element(*self.add_employee_loc).click()

#鼠标点击添加员工
    def add_createEmployee_click(self):
        self.find_element(*self.add_createEmployee_loc).click()
#添加员工字样判断
    def add_createEmployee(self):
         return self.find_element(*self.add_createEmployee_loc).text

#输入员工姓名
    def add_employeeName(self,name):
        self.find_element(*self.add_employeeName_loc).send_keys(name)
#点击入职时间文本框
    def add_employeeTime_click(self):
        self.find_element(*self.add_employeeTime_loc).click()
#选择入职时间
    def add_employeeTime_chose(self):
        self.find_element(*self.time_loc).click()

#输入工号
    def add_employeeNo(self,employeeNo):
        self.find_element(*self.add_employeeNo_loc).send_keys(employeeNo)

#输入手机号

    def add_employeePhone(self,phone):
        self.find_element(*self.add_employeePhone_loc).send_keys(phone)

#输入职位
    def add_employeePosition(self,position):
        self.find_element(*self.add_employeePosition_loc).send_keys(position)

# 点击入职时间文本框
    def add_employeeBornTime_click(self):
        self.find_element(*self.employeeBornTime_loc).click()
#点击出生时间文本框

    def add_employeeBornTime_click(self):
        self.find_element(*self.add_employeeBornTime_loc).click()

 # 选择出生时间
    def add_employeeBornTime_chose(self):
        self.find_element(*self.bornTime_loc).click()
#输入邮箱
    def add_employeeEmail(self,email):
        self.find_element(*self.add_employeeEmail_loc).send_keys(email)
#输入学历

    def add_employeeEducation(self,education):
        self.find_element(*self.add_employeeEducation_loc).send_keys(education)
#输入籍贯
    def add_employeeHome(self,home):
        self.find_element(*self.add_employeeHome_loc).send_keys(home)

#确认按钮

    def add_button(self):
        self.find_element(*self.add_employeeButton).click()
#关闭窗口

    def add_close(self):
        self.find_element(*self.add_closeButton).click()

#添加照片窗口
    def add_picture(self):
        self.find_element(*self.add_pictureButton).click()

#取消添加照片

    def add_cancel(self):
        self.find_element(*self.add_cancelButton).click()

#定义统添加员工接口

    def created(self,name,employeeNo,phone,position,email,home):
        self.add_createEmployee_click()
        self.add_employeeName(name)
        print(name)
        self.add_employeeTime_click()
        self.add_employeeTime_chose()
        self.add_employeeNo(employeeNo)
        print(employeeNo)
        self.add_employeePhone(phone)
        print(phone)
        self.add_employeePosition(position)
        self.add_employeeBornTime_click()
        self.add_employeebornTime_chose()
        self.add_employeeEmail(email)

        self.add_EmployeeHome(home)
        self.add_button()
        sleep(2)

    register_companyName_loc=(By.XPATH,"/html/body/div[2]/form/div[2]/span[2]")
    register_loginName_loc = (By.XPATH,"/html/body/div[2]/form/div[3]/span[2]")
    register_password_loc=(By.XPATH,"/html/body/div[2]/form/div[4]/span[2]")
    register_error_message=(By.XPATH,"/html/body/div[2]/form/div[6]")
#部门模块
    add_department_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/a")







#部门模块-添加部门
    # 填写名字
    add_departmentName_loc=(By.ID,"addTreeNode")
    #确定按钮
    add_departmentButton_loc=(By.ID,"addTreeNodeButton")
    #点击第一个平级部门的设置
    add_departmentSetting = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/span")
    add_departmentSetting_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li/span/a")
    add_departmentSetting2=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/ul/li/span")
    add_departmentSetting_loc2=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/ul/li/span/a")
    #点击第二个平级部门的设置
    add_departmentSetting_loc3 = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[2]/span/a")
    add_departmentSetting3= (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[2]/span")
    #下级部门
    add_departmentChildName_loc=(By.ID,"newStructrueName")
    add_departmentChild_loc=(By.CLASS_NAME,"newChild")
    add_departmentChildbutton_loc=(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div[3]/input[1]")
    #平级部门
    add_departmentSibling_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li/span/a/ul/li[2]")
    add_departmentSiblingName_loc = (By.ID,"newStructrueName")
    add_departmentSiblingbutton_loc = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div[3]/input[1]")
    #编辑部门
    add_departmentEditSelf_loc1=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/span/a/ul/li[3]")
    add_departmentEditSelf_loc2 = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/ul/li/span/a/ul/li[3]")
    add_departmentEditSelf_loc3 = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[2]/span/a/ul/li[3]")
    #编辑内容
    add_departmentEditName_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/span/input")
    add_departmentEditName_loc2 = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/ul/li/span/input")
    add_departmentEditName_loc3 = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[2]/span/input")
    add_departmentEditName_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/span/a[1]")
    add_departmentEditName_loc2 = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/ul/li/span/a[1]")
    add_departmentEditName_loc3 = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[2]/span/a[1]")

    #删除部门
    add_departmentDeleteSelf_loc1=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/span/a/ul/li[4]")
    add_departmentDeleteSelf_loc2 = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[1]/ul/li/span/a/ul/li[4]")
    add_departmentDeleteSelf_loc3 = ( By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li/ul/li[2]/span/a/ul/li[4]")
    add_departmentDeleteButton=(By.XPATH,"/html/body/div[1]/div[7]/div[2]/div[2]/div[2]/input[1]")
    #设置考勤
    add_departmentsetStructureRule_loc=(By.CLASS_NAME,"setStructureRule")

    def add_department(self):
        #建立部门
        self.find_element(*self.add_department_loc).click()
        self.find_element(*self.add_departmentName_loc).send_keys("测试部门")
        self.find_element(*self.add_departmentButton_loc).click()

        #建立下级部门

        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting_loc)).perform()
        self.find_element(*self.add_departmentChild_loc).click()

        self.find_element(*self.add_departmentChildName_loc).send_keys("测试部门_下级")
        self.find_element(*self.add_departmentChildbutton_loc).click()

    def add_departmentSibling(self):
        #建立平级部门
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting)).perform()
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting_loc)).perform()
        self.find_element(*self.add_departmentSibling_loc).click()
        self.find_element(*self.add_departmentSiblingName_loc).send_keys("测试部门_平级")
        self.find_element(*self.add_departmentSiblingbutton_loc).click()


    def edit_department(self):
        #编辑部门名
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting)).perform()
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting_loc)).perform()
        sleep(2)
        self.find_element(*self.add_departmentEditSelf_loc1).click()

        sleep(2)

        self.find_element(*self.add_departmentEditName_loc).send_keys("测试123")
        sleep(2)
        self.find_element(*self.add_departmentEditName_loc).click()
        sleep(2)
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting2)).perform()
        sleep(4)
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting_loc2)).perform()
        sleep(4)
        self.find_element(*self.add_departmentEditSelf_loc2).click()
        # self.find_element(*self.add_departmentEditName_loc).clear()
        self.find_element(*self.add_departmentEditName_loc2).send_keys("测试_下级")
        self.find_element(*self.add_departmentEditName_loc2).click()
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting3)).perform()
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting_loc3)).perform()
        self.find_element(*self.add_departmentEditSelf_loc3).click()
        # self.find_element(*self.add_departmentEditName_loc).clear()
        self.find_element(*self.add_departmentEditName_loc3).send_keys("测试_平级")
        self.find_element(*self.add_departmentEditName_loc3).click()





    def delete_department(self):
        #删除部门
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting2)).perform()
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting_loc2)).perform()
        self.find_element(*self.add_departmentDeleteSelf_loc2).click()
        self.find_element(*self.add_departmentDeleteButton).click()
        sleep(2)
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting3)).perform()
        sleep(2)
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting_loc3)).perform()
        sleep(2)
        self.find_element(*self.add_departmentDeleteSelf_loc3).click()
        sleep(2)
        self.find_element(*self.add_departmentDeleteButton).click()
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting)).perform()
        sleep(2)
        ActionChains(self.driver).move_to_element(self.find_element(*self.add_departmentSetting_loc)).perform()
        sleep(2)
        self.find_element(*self.add_departmentDeleteSelf_loc1).click()
        sleep(2)
        self.find_element(*self.add_departmentDeleteButton).click()












#编辑员工
class edit(Page):
    edit_employeeName_loc = (By.ID, "name1")
    edit_employeeTime_loc = (By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[1]/td[4]/span")
    edit_employeeTime_loc1 = (By.ID, "joinDate1")
    time_loc = (By.XPATH, "/html/body/div[4]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/span")
    edit_employeeNo_loc = (By.ID, "employeeNo1")
    edit_employeePhone_loc = (By.ID, "phone1")
    edit_employeeDepartment_loc = (By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/ul/input")
    edit_employeeSex_loc = (By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[3]/td[4]/ul/span")
    edit_employeePosition_loc = (By.ID, "position1")
    edit_employeeBornTime_loc = (By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[4]/td[4]/span")
    bornTime_loc = (By.XPATH, "/html/body/div[5]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[3]/span")
    edit_employeeEmail_loc = (By.ID, "email1")
    edit_employeeMarriage_loc = (By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[5]/td[4]/ul/span")
    edit_employeeEducation_loc = (By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/form/table/tbody/tr[6]/td[2]/ul/span")
    edit_employeeHome_loc = (By.ID, "home1")
    edit_Button = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[2]/div[4]/input[1]")
    edit_employeeButton_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[11]/div/a[1]")

#点击编辑按钮

    def edit_employeeButton(self):
        self.find_element(*self.edit_employeeButton_loc).click()


        # 修改员工姓名

    def edit_employeeName(self, name):
        self.find_element(*self.edit_employeeName_loc).clear()
        self.find_element(*self.edit_employeeName_loc).send_keys(name)

        # 获取员工姓名

    def edit_employeeName_text(self):
        return self.find_element(*self.edit_employeeName_loc).get_attribute('value')



        # 入职时间文本框

    def edit_employeeTime_click(self):
        self.find_element(*self.edit_employeeTime_loc).click()
        # 选择入职时间
    def edit_employeeTime_chose(self):
        self.find_element(*self.time_loc).click()

        #获取入职时间
    def edit_employeeTime_text(self):
        return self.find_element(*self.edit_employeeTime_loc).get_attribute('value')




        # 修改工号

    def edit_employeeNo(self, employeeNo):
        self.find_element(*self.edit_employeeNo_loc).clear()
        self.find_element(*self.edit_employeeNo_loc).send_keys(employeeNo)

       #获取员工号

    def edit_employeeNo_text(self):
        return self.find_element(*self.edit_employeeNo_loc).get_attribute('value')

        # 修改手机号

    def edit_employeePhone(self, phone):
        self.find_element(*self.edit_employeePhone_loc).clear()
        self.find_element(*self.edit_employeePhone_loc).send_keys(phone)

        #获取手机号

    def edit_employeePhone_text(self):
        return self.find_element(*self.edit_employeePhone_loc).get_attribute('value')

        # 修改职位

    def edit_employeePosition(self, position):
        self.find_element(*self.edit_employeePosition_loc).clear()
        self.find_element(*self.edit_employeePosition_loc).send_keys(position)

        #获取职位信息
    def edit_employeePosition_text(self):
        return self.find_element(*self.edit_employeePosition_loc).get_attribute('value')


        # 点击出生时间文本框

    def edit_employeeBornTime_click(self):
        self.find_element(*self.edit_employeeBornTime_loc).click()

        # 选择出生时间

    def edit_employeeBornTime_chose(self):
        self.find_element(*self.bornTime_loc).click()

        #获取出生日期

    def edit_employeeBornTime_text(self):
        return self.find_element(*self.edit_employeeBornTime_loc).get_attribute('value')

        # 修改邮箱
    def edit_employeeEmail(self, email):
        self.find_element(*self.edit_employeeEmail_loc).clear()
        self.find_element(*self.edit_employeeEmail_loc).send_keys(email)
        #获取邮箱信息
    def edit_employeeEmail_text(self):
        return self.find_element(*self.edit_employeeEmail_loc).get_attribute('value')

        # 修改学历

    def edit_employeeEducation(self, education):
        self.find_element(*self.edit_employeeEducation_loc).clear()
        self.find_element(*self.edit_employeeEducation_loc).send_keys(education)

        #获取学历信息

    def edit_employeeEducation_text(self):
        return self.find_element(*self.edit_employeeEducation_loc)


        # 修改籍贯

    def edit_employeeHome(self, home):
        self.find_element(*self.edit_employeeHome_loc).clear()
        self.find_element(*self.edit_employeeHome_loc).send_keys(home)
        #获取籍贯信息

    def edit_employeeHome_text(self):
        return self.find_element(*self.edit_employeeHome_loc).get_attribute('value')

        # 确认按钮

    def edit_button(self):
        self.find_element(*self.edit_Button).click()

#统一查看员工接口

    def edit_employee_text(self,employeeName,employeeTime,employeeNo,employeePhone,employeePosition,employeeBornTime,employeeEmail,employeeHome):
        self.edit_employeeButton()
        self.driver.assertEqual(self.edit_employeeName_text(),employeeName)
        self.driver.assertEqual(employeeTime,self.edit_employeeTime_text())
        self.driver.assertEqual(employeeNo,self.edit_employeeNo_text())
        self.driver.assertEqual(employeePhone,self.edit_employeePhone_text())
        self.driver.assertEqual(employeePosition,self.edit_employeePosition_text())
        self.driver.assertEqual(employeeBornTime,self.edit_employeeBornTime_text())
        self.driver.assertEqual(employeeEmail,self.edit_employeeEmail_text())

        self.assertEqual(employeeHome,self.edit_employeeHome_text())
        self.edit_button()
        sleep(3)

#统一修改接口

    def edit_employee(self,name,employeeNo,employeePhone,Position,email,home):
        self.edit_employeeButton()
        self.edit_employeeName(name)
        self.edit_employeeNo(employeeNo)
        self.edit_employeePhone(employeePhone)
        self.edit_employeePosition(Position)
        self.edit_employeeEmail(email)
        self.edit_employeeHome(home)
        self.edit_button()
#离职
    resign_employee_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[11]/div/a[2]")
    resign_employeebutton_loc=(By.XPATH,"/html/body/div[1]/div[7]/div[2]/div[2]/div[2]/input[1]")
    def resign_employee(self):
        self.find_element(*self.resign_employee_loc).click()

    def resgin_employeeButton(self):
        self.find_element(*self.resign_employeebutton_loc).click()



