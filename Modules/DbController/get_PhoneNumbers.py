#!/usr/bin/python
import json
import pymysql.cursors
import requests
from flask.json import JSONEncoder
import datetime

# Open database connection
def get_Phone(phone):

    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT Mobile from people where Mobile = %s "
            cursor.execute(sql,(phone, ))
            # test_func()
            data = cursor.fetchall()
            data1 =json.dumps(data)
            # print(data[0]["name"])
            if phone in data1:
                return 1
                print("chl gya")
            else :
                print("Nothing")
                return 0

    finally:
        connection.close()

def triggerPeople(name,Mobile,place):


    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)

    try :
        with connection.cursor() as cursor:
            sql = "INSERT into people (name,Mobile,place) values (%s,%s, %s)"
            cursor.execute(sql,(name,Mobile,place))
            # test_func()

        connection.commit()

    finally:
        connection.close()