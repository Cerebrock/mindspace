# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import os
from time import strftime
from flask_cors import CORS

exp_path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=exp_path)

CORS(app)

@app.route('/postdata', methods = ['POST'])
def get_data():
    data = request.form['data']
    
    with open(exp_path + '\data\\' + strftime('%Y-%m-%d %H-%M-%S') + ".json", 'a+') as out:
        out.write(data)

    return ''

if __name__ == '__main__':
    app.run(host="0.0.0.0")