# -*- coding:utf-8 -*-

class Languages(object):
  language = []

  class OverlapError(Exception):
    pass

  class Language(object):
    KEYS = ['name']

    def __init__(self, **kwargs):
      keys = Languages.Language.KEYS
      if not (set(keys) & set(kwargs.keys())):
        raise KeyError('name is must.')

      self.id = len(Languages.language) + 1
      self.name = kwargs.get('name')

      # option
      self.url = kwargs.get('url')

  def __init__(self):
    pass

  def __len__(self):
    return len(Languages.language)

  def __getitem__(self, index):
    if index > len(self):
      return IndexError('index abounds')

    return Languages.language[index] 

  def __getattr__(self, name):
    item = [e for e in Languages.language if e.name == name]
    if not item:
      raise AttributeError("{name} is not found".format(name=name))
    return item[0].id, item[0].name, item[0].url

  def __iadd__(self, others):
    l = Languages.Language(**others)

    for e in Languages.language:
      if e.name == l.name:
        raise Languages.OverlapError('language overlap')

    Languages.language.append(l)
    return self
