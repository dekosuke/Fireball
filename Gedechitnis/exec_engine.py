#/usr/bin/env python

#program execution engine

import os.path as op
import sys
if not '../' in sys.path:
  sys.path.insert(0, op.abspath(op.join(op.dirname(__file__), '../')))

import Capoeira.Language.base as l
import subprocess as subp

class ExecEngine(object):
  def __init__(self):
    pass
  def execCode(self, source, langname):
    lang = l.LangFactory().get(langname)
    exec_args = ["strace", "-o", "traceresult.txt", "timeout", "3"] + lang.get_exec_args()
    #print exec_args
    #exec program. we refered usage of subprocess
    #http://docs.python.org/library/subprocess.html#subprocess-replacements
    p = subp.Popen(exec_args, stdin=subp.PIPE, stdout=subp.PIPE)
    output = p.communicate(input=source)[0]
    return output


