import unittest,sys
sys.path.append('C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\')
from models import myunit
from page_obj.processPage import process
from page_obj.loginPage import login
from time import sleep


class processTest(myunit.MyTest):



    def test_process1(self):
        """点击流程管理:1,查看所有的流程"""
        login(self.driver).login("417155288@qq.com", "test1234")
        process(self.driver).process_click()
        process(self.driver).choose_date()
        process(self.driver).choose_allprocess()
        process(self.driver).choose_sickLeaveprocess()
        self.assertEqual(process(self.driver).detailType_text,"病假")
        process(self.driver).detail_close()
        sleep(2)
        process(self.driver).chooseissueLeaveprocess()
        # self.assertEqual(process(self.driver).processType_text, "事假")
        process(self.driver).choose_maternityLeaveprocess()
        # self.assertEqual(process(self.driver).processType_text, "年假")
        process(self.driver).choose_annualLeaveprocess()
        # self.assertEqual(process(self.driver).processType_text, "补签")
        process(self.driver).choose_retroactiveprocess()
        # self.assertEqual(process(self.driver).processType_text, "出差")
        process(self.driver).choose_outworkprocess()
        # self.assertEqual(process(self.driver).processType_text, "其他")
        process(self.driver).choose_otherLeaveLeaveprocess()
        # self.assertEqual(process(self.driver).processType_text, "特殊假")

if __name__=="__main__":
    unittest.main()
