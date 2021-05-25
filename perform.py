#!/usr/bin/python3.5
# coding:utf-8
from HTMLTestRunnerNew import HTMLTestRunner
import time,os,unittest

from .ApiTestCase.TianHongScrmApiTestCase import TianHongSCRMLoginTestCase

#调用实例化方法
s = unittest.TestSuite()
#调用实例化，多少个用例类，执行多少行实例化任务
s.addTests(unittest.TestLoader().loadTestsFromTestCase(TianHongSCRMLoginTestCase))
#时间挫
now = time.strftime('%Y-%m%d %H%M%S')
print(now)
#新建当前文件，并命名，执行写入操作
filename=open(os.getcwd() + '/resrResult' + 'now' + '.html','wb')
#报告标题抬头内容
runner = HTMLTestRunner(stream=filename,title= "TianHongAPI测试报告",description="API测试报告",tester= "Angela")
#执行操作
runner.run(s)