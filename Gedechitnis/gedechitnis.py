#!/usr/bin/env python
# -*- coding:utf-8 -*-

#exec-web api

from bottle import route, run, request

import exec_engine as e

@route("/exec", methods=['GET','POST'])
def index():
  if request.method in ['GET','POST']:
    src = request.args.get('src')
    lang = request.args.get('lang')
    engine = e.ExecEngine()
    output = engine.execCode(src, lang)
    return output
  else:
    return 'error-request not post'

if __name__ == '__main__':
  run(port=6677)
