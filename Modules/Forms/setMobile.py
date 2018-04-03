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
# from Modules import DbController
from DbController import createEntryStock
from DbController import get_PhoneNumbers
import webbrowser
from Services import ifPhone

class ReusableForm(Form):
    # sno =IntegerField('id', validators=[validators.required(),validators.input_required()])
    name = StringField(u'Name', validators=[validators.input_required()])
    phone = IntegerField(u'Mobile No', validators=[validators.input_required()])
    place = StringField(u'Place ', validators=[validators.input_required()])
    Submit = SubmitField()


def setPhone():
    form = ReusableForm(request.form)
    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        phone=request.form['phone']
        place=request.form['place']
        if form.validate():
            get_PhoneNumbers.triggerPeople(name,phone,place)
            print("Sucess")
        else:
            flash('Error: All the form fields are required. ')