from dapp import app
from flask import render_template, redirect
import json

@app.route('/')
def home_page():
    with open('.static/ERC721PresetMinterPauserAutoId.json', 'r') as f:
        abi = json.load(f)
        
    return render_template('home.html')