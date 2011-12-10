# -*- coding:utf-8 -*-

from language_base import *

class LangPerl(Language):
  def __init__(self):
    self.execargs = ["perl"] #option args for exec
    self.extention = ".pl"
