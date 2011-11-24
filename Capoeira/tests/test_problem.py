#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

if not '../' in sys.path:
  sys.path.insert(0, '../')

import unittest

from Mocaco.problem import Problems

class TestProglem(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testSet(self):
    p = Problems()
    p += {'alias': u'fizzbuzz', 
          'title': u'fizzbuzzを解いてください', 
          'description': 'がんばってくださいね'}

  def testGet(self):
    title = u'fizzbuzzをなるべく短く書いてください'
    description = u'無茶しやがって...'

    p = Problems()
    p += {'alias': u'fizzbuzz',
          'title': title, 
          'description': description}
    self.assertEquals(p.fizzbuzz, (title, description))

    with self.assertRaises(AttributeError):
      p.fibonacci

  def testLength(self):
    p = Problems()
    p += {'alias': u'fizzbuzz',
          'title': u'すごい問題', 
          'description': u'やったねうひょー'}
    p += {'alias': u'fibonacci',
          'title': u'素数を数えるよりは簡単じゃね',
          'description': u'1 1 2 3 5 8 13 21...'}

    self.assertTrue(2 == len(p))

  def testGetItem(self):
    p = Problems()
    p += {'alias': u'fizzbuzz',
          'title': u'すごい問題', 
          'description': u'やったねうひょー'}
    target = {
      'alias': u'fibonacci',
      'title': u'素数を数えるよりは簡単じゃね',
      'description': u'1 1 2 3 5 8 13 21...'}

    p += target
    t = Problems.Problem(**target)
    v = p[1]

    self.assertEqual(t.title, v.title)
    self.assertEqual(t.description, v.description)

  def testOverlap(self):
    p = Problems()
    problems= {
      'alias': u'fizzbuzz',
      'title': u'フィズバズ',
      'description': u'おなじみの問題ですね'}

    p += problems

    with self.assertRaises(Problems.OverlapError):
      p += problems

if __name__ == '__main__':
  unittest.main()
