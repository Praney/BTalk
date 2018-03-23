#!/usr/bin/python
import json
import pymysql.cursors
import requests
# Open database connection


def triggeroutStock(sno,itemid,outprice,date):
    global Serial
    global ItemId
    global InPrice
    global created_at
    Serial = sno
    ItemId = itemid
    outPrice = outprice
    sold_at = date


    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)

    try :
        with connection.cursor() as cursor:
            sql = "INSERT into outstock (sno,item_id,out_price,sold_at) values (%s,%s, %s,%s)"
            sql1="update instock set status=0 where sno="+Serial
            cursor.execute(sql, (Serial,ItemId,outPrice,sold_at))
            cursor.execute(sql1)
            # test_func()

        connection.commit()

    finally:
        connection.close()