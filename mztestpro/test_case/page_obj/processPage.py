from selenium.webdriver.common.by import By
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\TEST\\mztestpro\\test_case\\page_obj")
from base import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class process(Page):
    process_loc=(By.LINK_TEXT,"流程管理")
    startDate_loc=(By.XPATH,"//div[@class='dateInput clear']/span[1]/span/span")
    chooseDate_prevmonth=(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div[1]")
    chooseDate_predate=(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]")

    processType_loc=(By.XPATH,"//ul[@class='linkbutton linkbutton1']")
    allType_loc=(By.XPATH,"//ul[@class='linkbutton linkbutton1']/li[1]")
    sickLeaveType_loc = (By.XPATH, "//ul[@class='linkbutton linkbutton1']/li[2]")
    issueLeaveType_loc = (By.XPATH, "//ul[@class='linkbutton linkbutton1']/li[3]")
    maternityLeaveType_loc = (By.XPATH, "//ul[@class='linkbutton linkbutton1']/li[4]")
    annualLeaveType_loc = (By.XPATH, "//ul[@class='linkbutton linkbutton1']/li[5]")
    retroactiveType_loc = (By.XPATH, "//ul[@class='linkbutton linkbutton1']/li[6]")
    outworkType_loc = (By.XPATH, "//ul[@class='linkbutton linkbutton1']/li[7]")
    otherLeaveType_loc = (By.XPATH, "//ul[@class='linkbutton linkbutton1']/li[8]")
    specialType_loc = (By.XPATH, "//ul[@class='linkbutton linkbutton1']/li[9]")

#假的类型
    Leave_loc=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[7]/div/span")

    def processType_text(self):
        print(self.find_element(*self.Leave_loc).text)
        return self.find_element(*self.Leave_loc).text



    def process_click(self):
        self.find_element(*self.process_loc).click()
        sleep(2)

#选择时间
    def choose_date(self):
        self.find_element(*self.startDate_loc).click()
        sleep(1)
        self.find_element(*self.chooseDate_prevmonth).click()
        sleep(1)
        self.find_element(*self.chooseDate_prevmonth).click()
        sleep(1)
        self.find_element(*self.chooseDate_prevmonth).click()
        sleep(1)
        self.find_element(*self.chooseDate_predate).click()

#查看详情
    detail_loc=(By.ID,"datagrid-row-r1-2-0")
#详情中的请假类型
    detail_Type=(By.XPATH,"//div[@class='prointro']/div/span[2]")

    def detailType_text(self):
        return self.find_element(*self.detail_Type).text

#关闭详情
    detail_close_loc=(By.XPATH,"//div[@class='m-processDetails']/div[2]/div[1]/span")
    def detail_close(self):
        return self.find_element(*self.detail_close_loc).click()


#查看所有类型

    def choose_allprocess(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.processType_loc)).perform()
        sleep(2)
        self.find_element(*self.allType_loc).click()
        sleep(2)
        self.find_element(*self.detail_loc).click()
        sleep(2)

#查看所有病假类型
    def choose_sickLeaveprocess(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.processType_loc)).perform()
        sleep(2)
        self.find_element(*self.sickLeaveType_loc).click()
        sleep(2)
        self.find_element(*self.detail_loc).click()
        sleep(2)
#查看所有事假类型
    def chooseissueLeaveprocess(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.processType_loc)).perform()
        sleep(2)
        self.find_element(*self.issueLeaveType_loc).click()
        sleep(2)
        self.find_element(*self.detail_loc).click()
        sleep(2)

#查看所有产假类型
    def choose_maternityLeaveprocess(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.processType_loc)).perform()
        sleep(2)
        self.find_element(*self.maternityLeaveType_loc).click()
        sleep(2)
        self.find_element(*self.detail_loc).click()
        sleep(2)

#查看所有年假类型
    def choose_annualLeaveprocess(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.processType_loc)).perform()
        sleep(2)
        self.find_element(*self.annualLeaveType_loc).click()
        sleep(2)
        self.find_element(*self.detail_loc).click()
        sleep(2)

#查看所有补签类型
    def choose_retroactiveprocess(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.processType_loc)).perform()
        sleep(2)
        self.find_element(*self.retroactiveType_loc).click()
        sleep(2)
        self.find_element(*self.detail_loc).click()
        sleep(2)

#查看所有出差类型
    def choose_outworkprocess(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.processType_loc)).perform()
        sleep(2)
        self.find_element(*self.outworkType_loc).click()
        sleep(2)
        self.find_element(*self.detail_loc).click()
        sleep(2)

#查看所有其他假类型
    def choose_otherLeaveLeaveprocess(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.processType_loc)).perform()
        sleep(2)
        self.find_element(*self.otherLeaveType_loc).click()
        sleep(2)
        self.find_element(*self.detail_loc).click()
        sleep(2)


