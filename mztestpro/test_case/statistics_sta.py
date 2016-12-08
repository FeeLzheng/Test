import unittest,sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case")

from page_obj.loginPage import login
from page_obj.addPage import add
from page_obj.statisticsPage import statistics
from models import DB,function,myunit
from time import sleep


class statisticsTest(myunit.MyTest):
    """考勤统计"""
    # def test_statistics1(self):
    #     """1.1.1 点击考勤统计界面查看考勤"""
    #     login(self.driver).login("417155288@qq.com", "test1234")
    #     statistics(self.driver).statistics_click()
    #     statistics(self.driver).statisticsReport_click()
    #
    # def test_statistics2(self):
    #     """2.1.1 点击打卡记录查看考勤"""
    #     login(self.driver).login("417155288@qq.com", "test1234")
    #     statistics(self.driver).statistics_click()
    #     statistics(self.driver).statisticsCardReport_loc()


    # def test_statistics3(self):
    #     """2.1.2 点击打卡记查看员工打卡情况"""
    #     login(self.driver).login("417155288@qq.com", "test1234")
    #     statistics(self.driver).statistics_click()
    #     statistics(self.driver).statisticsCardReport_click()
    #     statistics(self.driver).organization_click()
    #     statistics(self.driver).dateStatistics_click()
    #
    # def test_statistics4(self):
    #     """3.1.1 点击当天打卡记查看员工打卡情况"""
    #     login(self.driver).login("417155288@qq.com", "test1234")
    #     statistics(self.driver).statistics_click()
    #     statistics(self.driver).statisticsOnedayCardReport_click()
    #     statistics(self.driver).onedayCardReport("1zheng_ceshi12")
    #     self.assertEqual(statistics(self.driver).employeeName_text(),"1zheng_ceshi12")

    # def test_statistics5(self):
    #     """4.1.1 点击报表导出查看导出报表界面"""
    #     login(self.driver).login("417155288@qq.com", "test1234")
    #     add(self.driver).add_department()
    #     add(self.driver).add_departmentSibling()
    #     statistics(self.driver).statistics_click()
    #     statistics(self.driver).statisticsOutput_click()
    def test_statistics6(self):
        """4.1.2 报表导出界面添加部门和删除部门"""
        login(self.driver).login("417155288@qq.com", "test1234")
        add(self.driver).add_department()
        add(self.driver).add_departmentSibling()
        statistics(self.driver).statistics_click()
        statistics(self.driver).statisticsOutput_click()
        statistics(self.driver).chooseDepartment()
        sleep(2)
        statistics(self.driver).deleteDepartment()
        sleep(2)
        add(self.driver).add_employee_click()
        add(self.driver).delete_department()






if __name__=="__main__":
    unittest.main()