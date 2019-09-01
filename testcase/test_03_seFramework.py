'''



'''

from selenium import webdriver
import time
import unittest
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# from libs.HTMLTestRunner_CN_Chart_Screen import HTMLTestRunner

class TestSearch03(unittest.TestCase):
    """测试类03"""
    def setUp(self):
        #每执行case都保持初始状态
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url='http://www.xqtesting.com'
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def test_05_search(self):
        """测试搜索的演示-05"""
        self.driver.get(self.base_url)
        self.driver.find_element("id","words").send_keys("自动化")
        self.driver.find_element("class name","btn-default").click()
    def test_06_search(self):
        """测试搜索的演示-06"""
        self.driver.get(self.base_url)
        self.driver.find_element("id","words").send_keys("脱口秀")
        self.driver.find_element("class name","btn-default").click()
