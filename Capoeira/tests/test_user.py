#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

if not '../' in sys.path:
  sys.path.insert(0, '../')

import unittest

from Mocaco.users import Users

class TestUser(unittest.TestCase):
  def setUp(self):
    Users.user = []

  def tearDown(self):
    pass

  def testSet(self):
    u = Users()
    u += {'name': u'ほげ'}

  def testGet(self):
    u = Users()
    u += {'name': u'うげ'}
    u += {'name': u'うひ'}

    self.assertEqual(u._1, (1, u'うげ'))
    self.assertEqual(u._2, (2, u'うひ'))

  def testGetItem(self):
    users = [
        {'name': u'どどど'},
        {'name': u'ギャオー'},
        {'name': u'うごごご'}
      ]

    u = Users()
    for e in users:
      u += e

    self.assertEqual(u[0].name, u'どどど')
    self.assertEqual(u[2].name, u'うごごご')

  def testOverlap(self):
    users = [
        {'name': u'ドワンド'},
        {'name': u'ニワンド'},
        {'name': u'ひー'}
      ]

    u = Users()
    for e in users:
      u += e

    with self.assertRaises(Users.OverlapError):
      u += users[0]

if __name__ == '__main__':
  unittest.main()
