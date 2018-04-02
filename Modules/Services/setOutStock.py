from __future__ import absolute_import
import sys
import time
from flask import Flask, json, jsonify, render_template, session, request, redirect, url_for, abort, session, flash
from flask_restful import Resource, Api
from flask import json
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
from DbController import triggeroutStock


class ReusableForm(Form):
    name =StringField('Name', validators=[validators.required(),validators.input_required()])
    sno =StringField('Tyre No', validators=[validators.required(),validators.input_required()])
    itemid =IntegerField('Item ID', validators=[validators.required(),validators.input_required()])
    outprice =IntegerField('Sale Price', validators=[validators.required(),validators.input_required()])
    givenprice =IntegerField('Given Price', validators=[validators.required(),validators.input_required()])
    date = DateField(u'Date ', )
    Submit = SubmitField()


def setOutStock():
    form = ReusableForm(request.form)
    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        sno=request.form['sno']
        itemid=request.form['itemid']
        outprice=request.form['outprice']
        givenprice=request.form['givenprice']
        date=request.form['date']

        if form.validate(): 
            triggeroutStock.triggeroutStock(name,sno,itemid,outprice,givenprice,date)
            print("success")
        else:
            flash('Error: All the form fields are required. ')