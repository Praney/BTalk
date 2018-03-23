#!/usr/bin/python
import json
import pymysql.cursors
import requests
from flask.json import JSONEncoder
import datetime

# Open database connection
class DateTimeEncoder(json.JSONEncoder):
    def default(self,data):
        if hasattr(data,'isoformat'):
            return data.isoformat()
        else:
            return json.JSONEncoder.default(self,data)

def getallitems():

    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT * from items "
            cursor.execute(sql)
            # test_func()
            data = cursor.fetchall()
            return json.dumps(data,cls=DateTimeEncoder)

    finally:
        connection.close()

def getallinstockitems():

    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT * from instock "
            cursor.execute(sql)
            # test_func()
            data = cursor.fetchall()
            return json.dumps(data,cls=DateTimeEncoder)

    finally:
        connection.close()

def getalloutstockitems():
    
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT * from outstock "
            cursor.execute(sql)
            # test_func()
            data = cursor.fetchall()
            return json.dumps(data,cls=DateTimeEncoder)

    finally:
        connection.close()

def getnoofitems():

    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='Business',
                             cursorclass=pymysql.cursors.DictCursor)
    try :
        with connection.cursor() as cursor:
            sql = "SELECT items.name,count(items.name) FROM instock JOIN items ON item_id = ID where status=1 group by items.name"
            cursor.execute(sql)
            # test_func()
            data = cursor.fetchall()
            return json.dumps(data,cls=DateTimeEncoder)

    finally:
        connection.close()
    
  

