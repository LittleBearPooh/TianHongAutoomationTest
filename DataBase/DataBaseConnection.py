#!/usr/bin/python3.5
# coding:utf-8

# 导入pymysql模块
import pymysql

def Add(sql,DBhost,DBport,DBuser,DBpassword,DBdb):

    # 连接database
    conn = pymysql.connect(host=DBhost, user=DBuser,password=DBpassword, port=DBport, db=DBdb,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    dbSQL=sql
    # sql = "insert INTO test.user (name,age,sex) VALUES (%s,%s,%s);"
    # username = "Alex"
    # age = 18
    # sex = "男"
    # 批量执行多条SQL记录插入时
    # sql = "INSERT INTO USER1(name, age) VALUES (%s, %s);"
    # data = [("Alex", 18), ("Egon", 20), ("Yuan", 21)]
    # try:
    #     # 批量执行多条插入SQL语句
    #     cursor.executemany(sql, data)
    #     # 提交事务
    #     conn.commit()

    try:
        # 执行SQL语句
        cursor.execute(dbSQL)
        # cursor.execute(sql, [username, age, sex])
        # 提交事务
        conn.commit()
        # 提交之后，获取刚插入的数据的ID
        id = cursor.lastrowid
        print(id)
        return id
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()



def delect(sql,DBhost,DBport,DBuser,DBpassword,DBdb):
    # 连接database
    conn = pymysql.connect(host=DBhost, user=DBuser,password=DBpassword, port=DBport, db=DBdb,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    dbSQL=sql
    # sql = "delete from test.user where id=%s"
    try:
        #执行sql
        cursor.execute(dbSQL)
        # cursor.execute(sql, [4])
        # 提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()

def Update(sql,DBhost,DBport,DBuser,DBpassword,DBdb):
    # 连接database
    conn = pymysql.connect(host=DBhost, user=DBuser,password=DBpassword, port=DBport, db=DBdb,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 修改数据的SQL语句
    dbSQL=sql
    # sql = "update test.user set age=%s where name=%s;"
    # username = "Alex"
    # age = 80
    try:
        # 执行SQL语句
        cursor.execute(dbSQL)
        # cursor.execute(sql, [age, username])
        # 提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()

def select(sql,DBhost,DBport,DBuser,DBpassword,DBdb):
    # 打开数据库连接
    db = pymysql.connect(host=DBhost, user=DBuser,password=DBpassword, port=DBport, db=DBdb,charset="utf8")

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    # 1.查询操作
    # 编写sql 查询语句  user 对应我的表名
    SelectSql = sql
    try:
        cur.execute(SelectSql)  # 执行sql语句
        results=cur.fetchone() #获取第一条响应结果数据
        return results
        # results = cur.fetchall()  # 获取查询的所有记录
        # print(results)
        # print("id", "name", "password")
        # 遍历结果
        # for row in results:
        #     id = row[0]
        #     name = row[1]
        #     password = row[2]
        #     print(id, name, password)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接
