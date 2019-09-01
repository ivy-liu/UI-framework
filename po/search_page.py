
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from base_page import BasePage

'''
该类主要是封装搜索页面的操作
'''
class SearchPage(BasePage):

	#访问>输入关键字>搜索
	def input_keyword_run(self,url,keywords):
		self.open_max(url)
		self.input('id--words',keywords)
		self.click_submit('class name--btn-default')

	#获取浏览器tilte
	def return_title(self):
		return self.get_title()


'''
from selenium import webdriver

driver = webdriver.Firefox()
sp = SearchPage(driver)
sp.input_keyword_run('http://www.xqtesting.com','测试帮日记')
print(sp.return_title())
'''
