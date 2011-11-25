# -*- coding:utf-8 -*-

class Solutions(object):
  class OverlapError(Exception):
    pass

  class Solution(object):
    KEYS = ['problem_id', 'input', 'output']

    def __init__(self, **kwargs):
      keys = Solutions.Solution.KEYS
      if set(keys) != set(kwargs.keys()):
        raise KeyError('{xs} and {x} is must.'.format(
                xs=','.join(keys[:-1]),
                x=keys[-1]
              ))
      self.problem_id = kwargs.get('problem_id')
      self.input = kwargs.get('input')
      self.output = kwargs.get('output')

  def __init__(self):
    self.solution = []

  def __len__(self):
    return len(self.solution)

  def __getitem__(self, index):
    if index > len(self):
      raise IndexError('index abounds')
    else:
      return self.solution[index]

  def __getattr__(self, _id):
    search_id = int(_id.replace('_',''))
    item = [e for e in self.solution if e.problem_id == search_id] 
    if not item:
      raise AttributeError("{_id} is not found".format(_id=_id))
    return search_id, item[0].input, item[0].output

  def __iadd__(self, other):
    s = Solutions.Solution(**other)
    for e in self.solution:
      if e.problem_id == s.problem_id:
        raise Solutions.OverlapError('solution overlap')

    self.solution.append(s)
    return self
