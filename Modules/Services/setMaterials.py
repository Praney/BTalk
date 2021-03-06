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


class ReusableForm(Form):
    # sno =IntegerField('id', validators=[validators.required(),validators.input_required()])
    name = StringField(u'Name', validators=[validators.input_required()])
    typeOf = StringField(u'typeOf', validators=[validators.input_required()])
    Company = SelectField('Type', choices=[('Apollo', 'Apollo'), ('Modi', 'Modi'), ('MRF', 'MRF'),('Others', 'Others')])
    Submit = SubmitField()


def setItem():
    form = ReusableForm(request.form)
    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        typeOf=request.form['typeOf']
        Company=request.form['Company']
        if form.validate():
            createEntryStock.triggerMaterials(name,typeOf,Company)
            print("success")
        else:
            flash('Error: All the form fields are required. ')