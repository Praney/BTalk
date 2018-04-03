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
from DbController import getallentries_instock
import webbrowser


def ifMaterial(sno):
    ispresent=getallentries_instock.get_tyreno_from_instockitems(sno)
    if ispresent == 1:
        url = 'http://localhost:8000/people/phone'
        webbrowser.open_new_tab(url)
    else :
        url = 'http://localhost:8000/inStock'
        webbrowser.open_new_tab(url)