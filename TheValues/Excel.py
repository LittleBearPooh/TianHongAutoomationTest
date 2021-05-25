#!/usr/bin/python3.5
# coding:utf-8

import xlrd

#定义取值的excel文本路径，接口入参取值excel中。采用excel维护脚本参数，采用坐标法取值，
def ReadExcel(x,y,z):
    openExcel=xlrd.open_workbook('E:/PythonProject/testM/APITestCase.xlsx').sheet_by_index(x).cell_value(y,z)
    return openExcel