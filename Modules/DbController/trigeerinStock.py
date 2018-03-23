#!/usr/bin/python
import json
import pymysql.cursors
import requests
# Open database connection


def triggerinStock(sno,itemid,inprice,date):
    global Serial
    global ItemId
    global InPrice
    global created_at
    Serial = sno
    ItemId = itemid
    InPrice = inprice
    created_at = date


    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)

    try :
        with connection.cursor() as cursor:
            sql = "INSERT into instock (sno,item_id,price,created_at) values (%s,%s, %s,%s)"
            cursor.execute(sql, (Serial,ItemId,InPrice,created_at))
            # test_func()

        connection.commit()

    finally:
        connection.close()