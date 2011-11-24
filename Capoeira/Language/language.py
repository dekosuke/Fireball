import language_python as langpy

class LangFactory():
  def __init__(self):
    pass
  def get_language(self, langname):
    if langname=="python":
      return langpy.LangPython()
    raise "language not found"

