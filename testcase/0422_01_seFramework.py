'''



'''

from selenium import webdriver
import time
import unittest
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tools.HTMLTestRunner_CN_Chart_Screen import HTMLTestRunner

class TestSearch(unittest.TestCase):
    """测试类"""
    def setUp(self):
        #每执行case都保持初始状态
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url='http://www.xqtesting.com'
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def test_01_search(self):
        """测试搜索的演示01"""
        self.driver.get(self.base_url)
        self.driver.find_element("id","words").send_keys("自动化")
        self.driver.find_element("class name","btn-default").click()
    def test_02_search(self):
        """测试搜索的演示02"""
        self.driver.get(self.base_url)
        self.driver.find_element("id","words").send_keys("脱口秀")
        self.driver.find_element("class name","btn-default").click()
report_path="test_folder\\result_htmlTestRunner.html"
all_suite=unittest.makeSuite(TestSearch)

fp=open(report_path,'wb')
runner=HTMLTestRunner(verbosity=2,stream=fp,title='UI自动化测试demo报告',description='test试试')

runner.run(all_suite)
fp.close()