#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import route, run

@route("/")
def index():
  return "index"
  #return render_template('index.html')

if __name__ == '__main__':
  run()
