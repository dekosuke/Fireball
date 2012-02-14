#!/usr/bin/env python
# coding:utf-8

from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

def modelTest():
  dbname = "hoge.db"
  os.system("rm "+dbname)
  engine = create_engine("sqlite:///"+dbname, echo=False)
  Session = sessionmaker(bind=engine)
  Base.metadata.create_all(engine) 
  problem1 = Problem("title", "description")
  user1 = User("hanako")
  session = Session()
  session.add(problem1)
  session.add(user1)
  session.commit()

if __name__ == "__main__":
  modelTest()
