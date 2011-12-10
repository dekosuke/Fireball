import language_python as langpy
import language_ruby as langrb
import language_perl as langperl
import language_php as langphp

class LangFactory():
  def __init__(self):
    pass
  def get(self, langname):
    if langname=="python":
      return langpy.LangPython()
    elif langname=="ruby":
      return langrb.LangRuby()
    elif langname=="perl":
      return langperl.LangPerl()
    elif langname=="php":
      return langphp.LangPHP()
    raise "language not found"

