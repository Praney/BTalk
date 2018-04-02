#!/usr/bin/python
import json
import pymysql.cursors
import requests
# Open database connection


def triggeroutStock(name,sno,itemid,outprice,givenprice,date):
    global Serial
    global ItemId
    global outPrice
    global sold_at
    global givenPrice
    global Name
    Name=name
    Serial = str(sno)
    ItemId = itemid
    outPrice = outprice
    givenPrice = givenprice
    sold_at = date
    left_price = int(outPrice)-int(givenPrice)


    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)

    try :
        with connection.cursor() as cursor:
            sql = "INSERT into outstock (sno,item_id,out_price,sold_at,given_price,name,left_price) values (%s,%s, %s,%s,%s,%s,%s)"
            sql1="update instock set status=0 where sno LIKE %s"
            cursor.execute(sql, (Serial,ItemId,outPrice,sold_at,givenPrice,Name,left_price))
            cursor.execute(sql1, (Serial, ))
            # cursor.execute(sql1)
            # test_func()

        connection.commit()

    finally:
        connection.close()