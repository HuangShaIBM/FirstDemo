'''
Created on 2017年4月7日

@author: Rose Huang
'''
from app import app
@app.route('/')
def index():
    return 'Hello Flask'