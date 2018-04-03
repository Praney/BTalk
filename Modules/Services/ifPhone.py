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
from DbController import get_PhoneNumbers
import webbrowser


def ifPhone(name,phone,place):
    ispresent=get_PhoneNumbers.get_Phone(name,phone,place)
    if ispresent == 1:
        print("Success")
    else :
        get_PhoneNumbers.triggerPeople(name,phone,place)

def checkPhone(phone):
    ispresent=get_PhoneNumbers.get_Phone(phone)
    if ispresent == 1:
        url = 'http://localhost:8000/outStock'
        webbrowser.open_new_tab(url)
    else :
        url = 'http://localhost:8000/people/signup'
        webbrowser.open_new_tab(url)