import language_python as langpy
import language_ruby as langrb

class LangFactory():
  def __init__(self):
    pass
  def get(self, langname):
    if langname=="python":
      return langpy.LangPython()
    elif langname=="ruby":
      return langrb.LangRuby()
    raise "language not found"

