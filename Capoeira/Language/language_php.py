# -*- coding:utf-8 -*-

from language_base import *

class LangPHP(Language):
  def __init__(self):
    self.execargs = ["php"] #option args for exec
    self.extention = ".php"
