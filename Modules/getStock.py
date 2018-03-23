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

#Initializing the App
app = Flask(__name__)
app.config['SECRET_KEY'] = 'automationqa'


class ReusableForm(Form):
    sno =IntegerField('id', validators=[validators.required(),validators.input_required()])
    name = StringField(u'Name', validators=[validators.input_required()])
    typeOf = SelectField('Type', choices=[('1', 'Truck Tyre'), ('2', 'Car Tyre'), ('3', 'Truck Tube'),('4', 'Car Tube')])
    InStock =IntegerField('In Stock', validators=[validators.required(),validators.input_required()])
    OutStock =IntegerField('Out Stock', validators=[validators.required(),validators.input_required()])
    Submit = SubmitField()


##########################################UI Route##########################################################
@app.route('/execute',methods=['GET','POST'])
def execute():
    form = ReusableForm(request.form)
    print (form.errors)
    if request.method == 'POST':
        sno=request.form['sno']
        name=request.form['name']
        typeOf=request.form['typeOf']
        InStock=request.form['InStock']
        OutStock=request.form['OutStock']
        if form.validate():
            remStock = int(InStock)-int(OutStock)
            print(remStock)
            print("success")
        else:
            flash('Error: All the form fields are required. ')
 
    # return 1
    return render_template('index.html', form=form)
        
if (__name__) == '__main__':
    	app.run(debug=True, host='localhost', port=8000)