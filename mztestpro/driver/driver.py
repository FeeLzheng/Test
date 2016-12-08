from selenium.webdriver import Remote
from selenium import webdriver

def browser():
    driver=webdriver.Firefox()

    driver.get("http://192.168.1.29:8888/SmartStage-Web")
    #driver.quit()
if __name__ == "__main__":
    dr = browser()
    #dr.get("http://www.baidu.com")
    dr.quit()