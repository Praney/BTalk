from __future__ import absolute_import
import sys
import time
from flask import Flask, json, jsonify, render_template, session, request, redirect, url_for, abort, session, flash
from flask_restful import Resource, Api
from flask import json
# from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
from flask_wtf import Form
from wtforms import *
import logging
import requests
import bunyan
import os
import uuid
import subprocess
from celery import Celery
# sys.path.append('../')
#from Modules import DbController
# from Modules import DbController
from DbController import createEntryStock
# import createEntryStock
from DbController import getallentries_instock
from Forms import setMaterials
from Forms import setInStock
from Forms import setOutStock
from Forms import ifTyreNo
from Forms import setMobile
from Forms import getMobile
import json
from json2html import *


#Initializing the App
app = Flask(__name__)
app.config['SECRET_KEY'] = 'automationqa'


##########################################UI Route##########################################################
@app.route('/materials',methods=['GET','POST'])
def execute():
    setMaterials.setItem()
    # return "success"
    return render_template('materials.html', form=setMaterials.ReusableForm(request.form))

@app.route('/ifinstock',methods=['GET','POST'])
def executematerialsinstock():
    ifTyreNo.ifIteminstock()
    # return "success"
    return render_template('materialsinstock.html', form=ifTyreNo.ReusableForm(request.form))

@app.route('/inStock',methods=['GET','POST'])
def executeinStock():
    setInStock.setInStock()
    return render_template('instock.html', form=setInStock.ReusableForm(request.form))

@app.route('/outStock',methods=['GET','POST'])
def executeoutStock():
    setOutStock.setOutStock()
    return render_template('outstock.html', form=setOutStock.ReusableForm(request.form))

@app.route('/allitems',methods=['GET','POST'])
def allitems():
    data = getallentries_instock.getallitems()
    html = json2html.convert(json=data)
    return html

@app.route('/instockitems',methods=['GET','POST'])
def allinstockitems():
    data = getallentries_instock.getallinstockitems()
    html = json2html.convert(json=data)
    return html

@app.route('/outstockitems',methods=['GET','POST'])
def alloutstockitems():
    data = getallentries_instock.getalloutstockitems()
    html = json2html.convert(json=data)
    return html

@app.route('/noofitems',methods=['GET','POST'])
def noofitems():
    data = getallentries_instock.getnoofitems()
    html = json2html.convert(json=data)
    return html    

@app.route('/people/phone',methods=['GET','POST'])
def ifPhone():
    getMobile.getPhone()
    return render_template('phone.html', form=setMobile.ReusableForm(request.form))

@app.route('/people/signup',methods=['GET','POST'])
def phone():
    setMobile.setPhone()
    return render_template('People_Signup.html', form=setMobile.ReusableForm(request.form))

if (__name__) == '__main__':
    app.run(debug=True,host = '0.0.0.0',port = 8000)
        