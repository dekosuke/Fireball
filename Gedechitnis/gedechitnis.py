#!/usr/bin/env python
# -*- coding:utf-8 -*-

#exec-web api

from flask import Flask
from flask import request,jsonify

import exec_engine as e

app = Flask(__name__)

@app.route("/exec", methods=['GET','POST'])
def index():
  if request.method in ['GET','POST']:
  #if request.method == 'POST' or True:
    #return str(request.form.keys())
    src = request.args.get('src')
    lang = request.args.get('lang')
    engine = e.ExecEngine()
    #return str((src,lang))
    output = engine.execCode(src, lang)
    return jsonify(stdout=output)
  else:
    return 'error-request not post'

if __name__ == '__main__':
  app.run(debug=True, port=8080)
