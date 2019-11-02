#!/usr/bin/python3

import pymysql

def get_info():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "147852369.6666", "meituan")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM meishi"

    #收集数据
    infos = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            title = row[2]
            avgprice = row[3]
            avgscore = row[4]
            address = row[7]
            # 打印结果
            info = {}
            info['title'] = title
            info['avgprice'] = avgprice
            info['avgscore'] = avgscore
            info['address'] = address
            infos.append(info)
            print("title=%s,avgprice=%s,avgscore=%s,address=%s" % \
                  (title, avgprice, avgscore, address))
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    return infos
