#!/usr/bin/python3.5
# coding:utf-8

from API.RequestInformation import RequestParameters,RequestHeader,RequestPath
from TheValues.Excel import ReadExcel
from DataBase.DataBaseConnection import select
import requests,unittest

#定义接口用例为测试类，并继承unittest框架的testcase类，当前类下面的方法需要test开头命名.测试用例类可以一个接口一个测试用例类
class TianHongSCRMLoginTestCase(unittest.TestCase):
    #当前接口执行未带数据库查询
    def test_ScrmLoginuser(self):
        try:
            # 调用requests的post方法执行接口，接口url、入参、请求头从excel的ReadExcel方法中读取，采用坐标法取值，也就是先读取shtte页，再读取行，再读取列。
            LoginuserResponse = requests.post(RequestPath(path=ReadExcel(0, 1, 1)),
                                              data=RequestParameters(formdata=ReadExcel(0, 1, 2)),
                                              headers=RequestHeader(HeaderData=ReadExcel(0, 1, 3)))
            if LoginuserResponse.json()['code']==200:
                print('接口相应成功，响应结果:',LoginuserResponse.json())
            elif LoginuserResponse.status_code != 200:
                print('接口服务调用失败，日志id：',LoginuserResponse.headers['X-B3-SpanId'])
            else:
                print("接口相应失败,响应结果：",LoginuserResponse.json(),'日志id：',LoginuserResponse.headers['X-B3-SpanId'])
        except Exception as e:
            raise e
    #当前接口执行带数据库查询
    def test_ScrmLoginuserDB(self):
        DBselect=select(sql=ReadExcel(2, 2, 5),DBhost=ReadExcel(1,1,1),DBpassword=ReadExcel(1,1,4),DBport=ReadExcel(1,1,2),DBuser=ReadExcel(1,1,3),DBdb=ReadExcel(1,1,5))
        try:
            # 调用requests的post方法执行接口，接口url、入参、请求头从excel的ReadExcel方法中读取，采用坐标法取值，也就是先读取shtte页，再读取行，再读取列。
            LoginuserResponse = requests.post(RequestPath(path=ReadExcel(0, 1, 1)),
                                              data=RequestParameters(formdata=ReadExcel(0, 1, 2)),
                                              headers=RequestHeader(HeaderData=ReadExcel(0, 1, 3)))
            #判断当前接口响应结果中的code是否等于200，等于再进行判断接口返回数据与数据库是否一致
            if LoginuserResponse.json()['code']==200:
                print('接口相应成功，响应结果:',LoginuserResponse.json())
                #判断接口响应结果与数据库查询结果是否一致，此处查询结果需要看不同数据库响应字段进行修改
                if DBselect[''] == LoginuserResponse.json()['msg']['name']:
                    print('数据库存在当前数据，接口相应成功，数据库结果为',DBselect)
                else:
                    print('数据库不存在当前结果数据，接口入参与数据库结果不一致，数据库结果为',DBselect)
            #判断当前接口状态码不等于200，不等于返回日志ID
            elif LoginuserResponse.status_code != 200:
                print('接口服务调用失败，日志id：',LoginuserResponse.headers['X-B3-SpanId'],'状态码为',LoginuserResponse.status_code)
            #当状态码等于200，接口响应code不等于200.返回响应参数，以及日志ID
            else:
                print("接口相应失败,响应结果：",LoginuserResponse.json(),'日志id：',LoginuserResponse.headers['X-B3-SpanId'])
        #接口执行异常，返回异常码
        except Exception as e:
            raise e