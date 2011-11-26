# -*- coding:utf-8 -*-

class Answers(object):
  answer = []

  class OverlapError(Exception):
    pass

  class Answer(object):
    KEYS = ['code', 'user_id', 
            'cpu_utilization', 'mem_utilization', 
            'elapsed_time', 'language_id', 'result']
    def __init__(self, **kwargs):
      keys = Answers.Answer.KEYS
      if set(keys) != set(kwargs.keys()):
        raise KeyError('{xs} and {x} is must.'.format(
                xs=','.join(keys[:-1]),
                x=keys[-1]
              ))
      self.id = len(Answers.answer) + 1
      self.code = kwargs.get('code')
      self.user_id = kwargs.get('user_id')
      self.cpu_utilization = kwargs.get('cpu_utilization')
      self.mem_utilization = kwargs.get('mem_utilization')
      self.elapsed_time = kwargs.get('elapsed_time')
      self.language_id = kwargs.get('language_id')
      self.result = kwargs.get('result')

  def __init__(self):
    pass

  def __len__(self):
    return len(Answers.answer)

  def __getitem__(self, index):
    if index > len(self):
      raise IndexError('answer abound')
    else:
      return Answers.answer[index]

  def __getattr__(self, _id):
    search_id = int(_id.replace('_', ''))
    item = [e for e in Answers.answer if e.id == search_id]
    if not item:
      raise AttributeError("{_id} is not found".format(_id=_id))
    r = item[0]
    return (search_id, 
            r.code,
            r.user_id,
            r.cpu_utilization,
            r.mem_utilization,
            r.elapsed_time,
            r.language_id,
            r.result)

  def __iadd__(self, others):
    a = Answers.Answer(**others)
    for e in Answers.answer:
      if e.id == a.id:
        raise Answers.OverlapError('answer overlap')

    Answers.answer.append(a)
    return self
