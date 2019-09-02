'''



'''

from selenium import webdriver
import time
import unittest
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from po.base_page import BasePage

class TestSearch02(unittest.TestCase):
    """王教授首页登陆02"""
    def setUp(self):
        #每执行case都保持初始状态
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url='https://www.prof.wang'
        self.bd=BasePage(self.driver)
        self.bd.open_max(self.base_url)
        
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_03_home_login(self):
        """首页-登录成功-写法1-03"""
        # self.bd.open(self.base_url)
        self.bd.click_submit('link text--登录')
        self.driver.implicitly_wait(5)
        self.bd.input('xpath--//input[contains(@placeholder,"邮箱/手机号")]',17621152203) 
        self.bd.input('xpath--//input[contains(@placeholder,"密码")]','qwe123123')
        time.sleep(5)
        self.bd.click_submit('xpath--//button')
        time.sleep(5)

    def test_04_home_login(self):
        '''首页-登录成功-写法2-04'''
        # self.bd.open(self.base_url)
        self.bd.link_text('登录')
        self.driver.implicitly_wait(5)
        self.bd.input('xpath--//*[@class="base-input"and@type="text"]',17621152203) 
        self.bd.input('xpath--//*[@class="base-input"and@type="password"]','qwe123123')
        time.sleep(3)
        self.bd.click_submit('class name--ivu-btn-text')
        self.driver.implicitly_wait(5)
        time.sleep(3)
        #登录成功，验证是否成功
        myname=self.bd.get_element('class name--account-name').text
        time.sleep(3)
        print('myname---',myname)

        try:
            self.assertIn('测试-刘',myname,'登录失败')
            print('登录成功，用户名是=',myname)      
        except Exception as e:
            print(e)
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise #捕获异常且不处理



        # self.driver.find_element_by_class_name('ivu-btn-text').click()
        # class="ivu-btn ivu-btn-text ivu-btn-long"
        