import language_python as langpy

class LangFactory():
  def __init__(self, langname):
    if langname=="python":
      return langpy.LangPython()
