# -*- coding:utf-8 -*-

class Problems(object):
  class OverlapError(Exception):
    pass

  class Problem(object):
    def __init__(self, **kwargs):
      if set(['alias', 'title', 'description']) != set(kwargs.keys()):
        raise KeyError('"title" and "description" is must.')

      self.alias = kwargs.get('alias')
      self.title = kwargs.get('title')
      self.description = kwargs.get('description')

  def __init__(self):
    self.problem = []

  def __len__(self):
    return len(self.problem)

  def __getitem__(self, index):
    if index > len(self.problem):
      raise IndexError('index abounds')
    else:
      return self.problem[index]

  def __getattr__(self, alias):
    item = [e for e in self.problem if e.alias == alias]
    if not item:
      raise AttributeError("{alias} not found".format(alias=alias)) 
    return item[0].title, item[0].description

  def __iadd__(self, other):
    p = Problems.Problem(**other)
    for e in self.problem:
      if e.alias == p.alias:
        raise Problems.OverlapError('problem overlap')

    self.problem.append(Problems.Problem(**other))
    return self

