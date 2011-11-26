# -*- coding:utf-8 -*-

class Users(object):
  user = []

  class OverlapError(Exception):
    pass

  class User(object):
    KEYS = ['name']
    def __init__(self, **kwargs):
      keys = Users.User.KEYS
      if set(keys) != set(kwargs.keys()):
        raise KeyError('name is must.')

      self.id = len(Users.user) + 1
      self.name = kwargs.get('name')

  def __init__(self):
    pass

  def __len__(self):
    return len(Users.user)

  def __getitem__(self, index):
    if index > len(self):
      raise IndexError('index abounds')
    else:
      return Users.user[index]

  def __getattr__(self, _id):
    search_id = int(_id.replace('_', ''))
    item = [e for e in Users.user if e.id == search_id]
    if not item:
      raise AttributeError("{_id} is not found".format(_id=_id))
    return search_id, item[0].name

  def __iadd__(self, other):
    u = Users.User(**other)
    for e in Users.user:
      if u.name == e.name:
        raise Users.OverlapError('user overlap')

    Users.user.append(u)
    return self
