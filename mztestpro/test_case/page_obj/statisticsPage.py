from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# import sys
# sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\page_obj")
from base import Page
from time import sleep


class statistics(Page):
    """考勤统计界面"""
    statistics_loc=(By.LINK_TEXT,"考勤统计")
    statisticsReport_loc=(By.XPATH,"//div[@id='attendance']/div/div[1]/div[3]/ul/li[1]/a")
    statisticsCardReport_loc = (By.XPATH, "//div[@id='attendance']/div/div[1]/div[3]/ul/li[2]/a")
    statisticsOnedayCardReport_loc = (By.XPATH, "//div[@id='attendance']/div/div[1]/div[3]/ul/li[3]/a")
    statisticsOutput_loc = (By.XPATH, "//div[@id='attendance']/div/div[1]/div[3]/ul/li[4]/a")




# 点击考勤统计导航栏

    def statistics_click(self):
        self.find_element(*self.statistics_loc).click()


#点击考勤报表导航栏

    def statisticsReport_click(self):
        self.find_element(*self.statisticsReport_loc).click()

#点击打卡记录导航栏

    def statisticsCardReport_click(self):
        self.find_element(*self.statisticsCardReport_loc).click()

#点击当日打卡导航栏

    def statisticsOnedayCardReport_click(self):
        self.find_element(*self.statisticsOnedayCardReport_loc).click()

 # 点击导出报表导航栏

    def statisticsOutput_click(self):
        self.find_element(*self.statisticsOutput_loc).click()




    allCompany_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/ul/span/span[2]/img")
    employee_loc = (By.XPATH, "//span[@title='1zheng_ceshi12']")
    date_search_loc=(By.LINK_TEXT,"按日期统计")
    month_search_loc = (By.LINK_TEXT, "统计本月")
    lastmonth_search = (By.LINK_TEXT, "统计上月")

# 点击组织架构

    def organization_click(self):
        self.find_element(*self.allCompany_loc).click()
        sleep(2)
        self.find_element(*self.employee_loc).click()
        sleep(2)

# 点击日期统计

    def dateStatistics_click(self):
        self.find_element(*self.date_search_loc).click()
        sleep(2)
        self.find_element(*self.month_search_loc).click()
        sleep(2)
        self.find_element(*self.lastmonth_search).click()
        sleep(2)
        #确保点击时不会出现其他错误，再次点击组织架构
        self.find_element(*self.employee_loc).click()

#当天打卡记录中的搜索功能

    rearchCondition=(By.ID,"searchCondition")
    rearchCondition_employeeName=(By.XPATH,"//*[@id='searchCondition']/li[1]")
    employeeRearch_loc=(By.ID,"searchInput")
    employeeRearchButton_loc=(By.ID,"searchForPerson")
    employeeName_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/table/tbody/tr/td[1]/div")

    def onedayCardReport(self,name):
        sleep(2)
        ActionChains(self.driver).move_to_element(self.find_element(*self.rearchCondition)).perform()
        sleep(2)
        self.find_element(*self.rearchCondition_employeeName).click()
        sleep(2)
        self.find_element(*self.employeeRearch_loc).send_keys(name)
        self.find_element(*self.employeeRearchButton_loc).click()

    def employeeName_text(self):
        return self.find_element(*self.employeeName_loc).text

#导出表报内的功能

    addDepartmentButton_loc=(By.XPATH,"//a[@title='添加部门']")
    addDepartment_loc = (By.XPATH, "//input[@placeholder='一次可选择多个部门']")
    chooseDepartment_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[4]/div/div[2]/div[1]/div[3]/div/ul/div[2]/div[2]/div/div[1]/div/div/ul/li[1]/span")
    chooseDepartmentButton_loc=(By.LINK_TEXT,"确定")
    deleteDepartment_loc=(By.XPATH,"//a[@class='deleteStructrue' and @title='删除']")
    deleteDepartmentButton_loc=(By.XPATH,"//Input[@class='clickButton buttonTrue' and @value='确定']")

    def chooseDepartment(self):
        self.find_element(*self.addDepartmentButton_loc).click()
        self.find_element(*self.addDepartment_loc).click()
        self.find_element(*self.chooseDepartment_loc).click()
        self.find_element(*self.chooseDepartmentButton_loc).click()


    def deleteDepartment(self):
        self.find_element(*self.deleteDepartment_loc).click()
        self.find_element(*self.deleteDepartmentButton_loc).click()

