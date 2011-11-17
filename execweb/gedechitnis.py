#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return 'Fire Ball'

def execProblem(lang, inputs, outputs):
  pass
  #foreach problem, run exec and if all pass ok

if __name__ == '__main__':
  app.run()
