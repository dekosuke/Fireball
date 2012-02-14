from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Problem(Base):
  __tablename__ = 'problems'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  description = Column(String)
  created_at = Column(DateTime)
  updated_at = Column(DateTime)

  def __init__(self, title, description):
    self.title = title
    self.description

class TestCase(Base):
  __tablename__ = 'testcases'

  id = Column(Integer, primary_key=True)
  problem_id = Column(Integer)
  input = Column(String)
  output = Column(String)

  def __init__(self, problem_id, input, output):
    self.problem_id = problem_id
    self.input = input
    self.output = output

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)

  def __init__(self, name):
    self.name = name

class Answer(Base):
  __tablename__ = 'answers'

  id = Column(Integer, primary_key=True)
  code = Column(String)
  user_id = Column(Integer)
  language = Column(String)
  result = Column(String)

  def __init__(self, **kwargs):
    self.code = kwargs.get('code')
    self.user_id = kwargs.get('user_id')
    self.language = kwargs.get('language')
    self.result = kwargs.get('result')

