from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)
from dapp import routes
