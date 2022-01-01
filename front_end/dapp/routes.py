from dapp import app
from flask import render_template, redirect
import json

with open('/Users/eliafrank/Desktop/Projects/web3/nft_minter/front_end/dapp/static/ERC721PresetMinterPauserAutoId.json', 'r') as f:
    abi = json.load(f)['abi']

@app.route('/')
def home_page():
    nft_abi = abi
    return render_template('home.html', nft_abi=nft_abi)