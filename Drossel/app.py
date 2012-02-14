#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import route, template, static_file, debug, run

DEBUG = True
RELOAD = True

@route('/')
def index():
  return template('index')

@route('/static/<path:path>')
def static(path):
  return static_file(path, 'static')

if __name__ == '__main__':
  debug(DEBUG)
  run(host='localhost', port=8080, reloader=RELOAD)
