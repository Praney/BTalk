#!/usr/bin/python
import json
import pymysql.cursors
import requests
# Open database connection


def gettriggerMaterials(name,typeOf,Company):
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
            sql = "SELECT name from items where name = %s"
            cursor.execute(sql,(name, ))
            # test_func()
            data = cursor.fetchall()
            data1 =json.dumps(data)
            # print(data[0]["name"])
            if name in data1:
                return 1
                print("chl gya")
            else :
                print("Nothing")
                return 0

    finally:
        connection.close()

# x=gettriggerMaterials("XMR","A","B")
# print(x)

def settriggerMaterials(name,typeOf,Company):
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