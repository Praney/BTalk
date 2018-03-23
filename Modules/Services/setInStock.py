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
from DbController import createEntryStock
from DbController import trigeerinStock
# from wtforms_components
# from flask.ext.admin.form.widgets import DatePickerWidget
# from flask.ext.admin.form.widgets import DatePickerWidget


class ReusableForm(Form):
    sno =IntegerField('Serial No', validators=[validators.required(),validators.input_required()])
    itemid =IntegerField('Item ID', validators=[validators.required(),validators.input_required()])
    inprice =IntegerField('In Price', validators=[validators.required(),validators.input_required()])
    date = DateField(u'Date ', )
    Submit = SubmitField()


def setInStock():
    form = ReusableForm(request.form)
    print (form.errors)
    if request.method == 'POST':
        sno=request.form['sno']
        itemid=request.form['itemid']
        inprice=request.form['inprice']
        date=request.form['date']

        if form.validate():
            trigeerinStock.triggerinStock(sno,itemid,inprice,date)
            print("success")
        else:
            flash('Error: All the form fields are required. ')