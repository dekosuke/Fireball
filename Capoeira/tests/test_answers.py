#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

if not '../' in sys.path:
  sys.path.insert(0, '../')

import unittest

from Mocaco.answers import Answers

class TestAnswers(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    Answers.answer = []

  def testSet(self):
    a = Answers()
    a += {'code': u'print (lambda x: x + 1)(100)',
          'user_id': 1, 
          'cpu_utilization': 45,
          'mem_utilization': 2048,
          'elapsed_time': 200,
          'language_id': u'python',
          'result': u'101'
         }

  def testGet(self):
    a = Answers()
    a += {'code': u'print (lambda x: x + 1)(100)',
          'user_id': 1,
          'cpu_utilization': 45,
          'mem_utilization': 2048,
          'elapsed_time': 200,
          'language_id': u'python',
          'result': u'101'
         }

    self.assertEquals(a._1, 
        (1, 
         u'print (lambda x: x + 1)(100)',
         1,
         45,
         2048,
         200,
         u'python',
         u'101')
        )

  def testGetItem(self):
    answers = [
        {
         'code': u'print (lambda x: x + 1)(100)',
         'user_id': 1, 
         'cpu_utilization': 45,
         'mem_utilization': 2048,
         'elapsed_time': 200,
         'language_id': u'python',
         'result': u'101'
        },
        {
         'code': 
           u'"".join((str(e) for e in range(100) if e%3 == 0 and e%5 == 0))',
         'user_id': 2, 
         'cpu_utilization': 20,
         'mem_utilization': 1024,
         'elapsed_time': 100,
         'language_id': u'python',
         'result': u'0153045607590'
        },
        {
         'code': u'<?php echo HELLOWORLD;',
         'user_id': 3,
         'cpu_utilization': 3,
         'mem_utilization': 1024,
         'elapsed_time': 200,
         'language_id': u'php',
         'result': 'HELLOWORLD'
        }
      ]
    a = Answers()
    for e in answers:
      a += e

    v = a[0]
    t = Answers.Answer(**answers[0])

    self.assertEquals(v.code, t.code)
    self.assertEquals(v.user_id, t.user_id)
    self.assertEquals(v.cpu_utilization, t.cpu_utilization)
    self.assertEquals(v.mem_utilization, t.mem_utilization)
    self.assertEquals(v.elapsed_time, t.elapsed_time)
    self.assertEquals(v.language_id, t.language_id)
    self.assertEquals(v.result, t.result)

  def testLength(self):
    answers = [
        {
         'code': u'print (lambda x: x + 1)(100)',
         'user_id': 1, 
         'cpu_utilization': 45,
         'mem_utilization': 2048,
         'elapsed_time': 200,
         'language_id': u'python',
         'result': u'101'
        },
        {
         'code': 
           u'"".join((str(e) for e in range(100) if e%3 == 0 and e%5 == 0))',
         'user_id': 2, 
         'cpu_utilization': 20,
         'mem_utilization': 1024,
         'elapsed_time': 100,
         'language_id': u'python',
         'result': u'0153045607590'
        },
        {
         'code': u'<?php echo HELLOWORLD;',
         'user_id': 3,
         'cpu_utilization': 3,
         'mem_utilization': 1024,
         'elapsed_time': 200,
         'language_id': u'php',
         'result': 'HELLOWORLD'
        }
      ]
    a = Answers()
    for e in answers:
      a += e

    self.assertEquals(len(a), 3)

  def testOverlap(self):
    pass

if __name__ == '__main__':
  unittest.main()
