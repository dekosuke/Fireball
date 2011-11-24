# -*- coding:utf-8 -*-

from language_base import *

class LangPython(Language):
  def __init__(self):
    self.execargs = ["python"] #option args for exec
    self.extention = ".py"
