#!/usr/bin/python3.5
# coding:utf-8
import pymysql

#定义请求的URL，路径，通过path取值
def RequestPath(path):
    url=path
    return url

#定义接口的入参，通过body取值
def RequestParameters(formdata):
    Parameters=formdata
    return Parameters

#定义接口请求头部，通过data取值
def RequestHeader(HeaderData):
    headers=HeaderData
    return headers
