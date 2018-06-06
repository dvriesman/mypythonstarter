#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api',methods=['POST'])
def createEmp(): 

    lang = request.json['language']
    if lang == 'python':
        result = jsonify({'result':'That\'s nice, but slow.'})
    else:
        if lang == 'java':
            result = jsonify({'result':'Faster than python!'})
        else:
            result = jsonify({'result':'No comments'})
    
    return result


if __name__ == "__main__":

     app.run(host='0.0.0.0')
