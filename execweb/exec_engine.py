#/usr/bin/env python

#program execution engine

import Capoeira.Cadeira.language as l

class ExecEngine(object):
  def __init__(self):
    pass
  def exec(source, langname):
    result = new ExecResult()
    lang = l.LangFactory(langname)
    exec_str = lang.get_exec_str(source)
    #exec pr`ogram
    result_str = ...
    result = lang.parse_result_str(result_str)
    return result
