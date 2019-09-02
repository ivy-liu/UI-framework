'''



'''

from selenium import webdriver
import time
import unittest
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from po.base_page import BasePage
from po.search_page import SearchPage

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

    def test_search_seccess(self):
        '''搜索 演示成功'''
        keywords='自动化'
        sp=SearchPage(self.driver)
        sp.input_keyword_run(self.base_url,keywords)
        try:
            self.assertIn(keywords,sp.return_title(),'查询失败')
            print('成功，搜索的关键字=',keywords)
        except Exception as e:
            print(e)
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise #捕获异常且不处理
    def test_search_failure(self):
        '''搜索 演示失败'''
        keywords='自动化'
        sp=SearchPage(self.driver)
        sp.input_keyword_run(self.base_url,keywords)
        try:
            self.assertIn(keywords,'2','查询失败')
            print('失败，搜索的关键字=',keywords)
        except Exception as e:
            print(e)
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise #捕获异常且不处理

