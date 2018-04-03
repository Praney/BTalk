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
import webbrowser


def ifMaterial(name,typeOf,Company):
    ispresent=createEntryStock.gettriggerMaterials(name,typeOf,Company)
    if ispresent == 1:
        url = 'http://localhost:8000/ifinstock'
        webbrowser.open(url,new=0)
    else :
        createEntryStock.settriggerMaterials(name,typeOf,Company)