#/usr/bin/env python

#program execution engine

import os.path as op
import sys
if not '../' in sys.path:
  sys.path.insert(0, op.abspath(op.join(op.dirname(__file__), '../')))

import Capoeira.Language.language as l
import subprocess as subp

class ExecEngine(object):
  def __init__(self):
    pass
  def execCode(self, source, langname):
    lang = l.LangFactory().get_language(langname)
    exec_args = lang.get_exec_args()
    #exec program. we refered usage of subprocess
    #http://docs.python.org/library/subprocess.html#subprocess-replacements
    print exec_args
    p = subp.Popen(exec_args, stdin=subp.PIPE, stdout=subp.PIPE)
    output = p.communicate(input=source)[0]
    return output

#here is example and soon deleted
if True:
  e = ExecEngine()
  r =e.execCode("print 'test'", "python")
  print "result is:\n"+r
