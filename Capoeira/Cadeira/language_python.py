# -*- coding:utf-8 -*-

from language_base import *

class LangPython(Language):
  def __init__(self):
    self.exec = "python27"
    self.execargs = [] #option args for exec
    self.extention = ".py"
  def parseResult(self): #parse result of execution. used by execution server
    pass
