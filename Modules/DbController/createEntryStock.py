#!/usr/bin/python
import json
import pymysql.cursors
import requests
# Open database connection


def triggerMaterials(name,typeOf,Company):
    global nameMat
    global typeOff
    global CompanyMat
    nameMat = name
    typeOff = typeOf
    CompanyMat = Company


    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)

    try :
        with connection.cursor() as cursor:
            sql = "INSERT into items (name,type,Company) values (%s,%s, %s)"
            cursor.execute(sql, (nameMat,typeOff ,CompanyMat))
            # test_func()

        connection.commit()

    finally:
        connection.close()

# def test_func():
#     print (nameMat)
#     print (CompanyMat)

# triggerMaterials("C","D")

# disconnect from server
