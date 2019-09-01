
import time
import unittest
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from libs.HTMLTestRunner_CN_Chart_Screen import HTMLTestRunner


#定义用例存放地址
base_path=os.path.dirname(os.path.abspath(__file__))    
casePath=base_path+"\\testcase\\"
#定义测试结果存放路径
result=base_path+'\\report\\'
# print('result--',result)

def CreatSuite():
    #定义单元测试容器
    testUnit=unittest.TestSuite()
    #获取用例文件
    discover=unittest.defaultTestLoader.discover(casePath,pattern='test_*.py',top_level_dir=None)
    #把用例加入容器
    for testSuite in discover:
        for caseName in testSuite:
            print(caseName)
            testUnit.addTest(caseName)
            time.sleep(4)
            # print('testUnit---',testUnit)报错原因，py文件名中有一个空格
            
    return testUnit

testCase=CreatSuite()


def gettime():
    nowtime=time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
    return nowtime
def getday():
    day=day=time.strftime('%Y-%m-%d', time.localtime())
    return day


#获取系统当前时间
now=gettime()
day=getday()
#定义单个测试报告存放地址
single_report=result+'\\'+day
fileName=single_report+'\\'+now+'_result.html'
if os.path.exists(single_report):
    
    fp=open(fileName,'wb')
    try:
        #定义报告
        runner=HTMLTestRunner(verbosity=2,stream=fp,title='UI自动化测试demo报告',description='描述test试试')
        #运行测试用例
        runner.run(testCase)
        # fp.flush()#缓存写进文件，等下试试不写，不要也可以，没毛病
    except Exception as e:
        print(e)
    finally:
        fp.close()
else:
    try:
        os.mkdir(result)
    except Exception as e:
        pass
    try:
        os.mkdir(single_report)
    except Exception as e:
        pass
    fp=open(fileName,'wb')
    try:
        #定义报告
        runner=HTMLTestRunner(verbosity=2,stream=fp,title='UI自动化测试demo报告',description='描述test试试')
        #运行测试用例
        runner.run(testCase)
        # fp.flush()#缓存写进文件，等下试试不写，不要也可以，没毛病
    except Exception as e:
        print(e)
    finally:
        fp.close()


